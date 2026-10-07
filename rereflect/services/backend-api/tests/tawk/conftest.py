"""Exercise tawk routes with real auth/DB, without unrelated native SAML imports."""
import os
os.environ.setdefault("JWT_SECRET", "isolated-tawk-tests-only")
os.environ["CACHE_ENABLED"] = "false"

import importlib
import uuid
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from src.models import Base, Organization, User
from src.database.session import get_db
from src.api.auth import create_access_token, hash_password


@pytest.fixture(scope="session")
def postgres_engine():
    url = os.getenv("TAWK_TEST_DATABASE_URL")
    if not url:
        yield None
        return
    schema = "fs_tawk_test_" + uuid.uuid4().hex
    admin = create_engine(url, connect_args={"connect_timeout": 10})
    with admin.begin() as conn:
        conn.execute(text(f'CREATE SCHEMA "{schema}"'))
    engine = create_engine(url, connect_args={"connect_timeout": 10, "options": f"-csearch_path={schema}"})
    tables = [Base.metadata.tables[name] for name in (
        "organizations", "users", "integrations", "feedback_sources", "feedback_items",
        "feedback_source_events", "tawk_integrations")]
    try:
        Base.metadata.create_all(engine, tables=tables)
        yield engine
    finally:
        engine.dispose()
        with admin.begin() as conn:
            conn.execute(text(f'DROP SCHEMA "{schema}" CASCADE'))
        admin.dispose()


@pytest.fixture
def db(postgres_engine):
    engine = postgres_engine or create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
    if postgres_engine:
        with engine.begin() as conn:
            conn.execute(text('TRUNCATE tawk_integrations, feedback_source_events, feedback_items, feedback_sources, integrations, users, organizations RESTART IDENTITY CASCADE'))
    else:
        Base.metadata.create_all(engine)
    with sessionmaker(bind=engine)() as session:
        yield session
    if not postgres_engine: engine.dispose()


@pytest.fixture
def client(db):
    app = FastAPI()
    from src.api.routes.feedback_sources import router
    app.include_router(router)
    for name in ("tawk_integration", "tawk_webhook"):
        module = importlib.import_module("src.api.routes." + name)
        app.include_router(module.router)
    app.dependency_overrides[get_db] = lambda: db
    with TestClient(app) as c:
        yield c


@pytest.fixture
def auth_headers(db):
    org = Organization(name="Owner test", plan="pro")
    db.add(org); db.flush()
    user = User(email="owner@example.com", role="owner", organization_id=org.id,
                password_hash=hash_password("testpassword"))
    db.add(user); db.commit()
    return {"Authorization": "Bearer " + create_access_token({
        "user_id": user.id, "organization_id": org.id, "role": "owner"})}


@pytest.fixture
def member_headers(db):
    org = Organization(name="Member test", plan="pro")
    db.add(org); db.flush()
    user = User(email="member@example.com", role="member", organization_id=org.id,
                password_hash=hash_password("testpassword"))
    db.add(user); db.commit()
    return {"Authorization": "Bearer " + create_access_token({
        "user_id": user.id, "organization_id": org.id, "role": "member"})}
