"""Owner bootstrap against a real isolated DB; no cloud or broker required."""

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src import seed
from src.api.auth import verify_password
from src.models import Base, Organization, User


@pytest.fixture
def database(tmp_path, monkeypatch):
    engine = create_engine(f"sqlite:///{tmp_path / 'bootstrap.sqlite'}")
    Base.metadata.create_all(engine, tables=[Organization.__table__, User.__table__])
    sessions = sessionmaker(bind=engine)
    monkeypatch.setattr(seed, "SessionLocal", sessions)
    monkeypatch.delenv("ADMIN_EMAIL", raising=False)
    monkeypatch.delenv("ADMIN_PASSWORD", raising=False)
    yield sessions
    engine.dispose()


@pytest.mark.parametrize(
    "email,password",
    [(None, None), ("owner@example.com", None), (None, "test-only-password"),
     ("   ", "test-only-password"), ("owner@example.com", "   ")],
)
def test_fresh_database_requires_explicit_credentials(database, monkeypatch, email, password):
    if email is not None:
        monkeypatch.setenv("ADMIN_EMAIL", email)
    if password is not None:
        monkeypatch.setenv("ADMIN_PASSWORD", password)

    with pytest.raises(RuntimeError, match="ADMIN_EMAIL.*ADMIN_PASSWORD"):
        seed.seed_admin_user()

    with database() as db:
        assert db.query(User).count() == 0
        assert db.query(Organization).count() == 0


def test_explicit_owner_credentials_create_one_account(database, monkeypatch):
    monkeypatch.setenv("ADMIN_EMAIL", "aayaannkausar@gmail.com")
    monkeypatch.setenv("ADMIN_PASSWORD", " test-only-owner-password ")
    seed.seed_admin_user()
    seed.seed_admin_user()

    with database() as db:
        owner = db.query(User).one()
        assert owner.email == "aayaannkausar@gmail.com"
        assert owner.role == "owner"
        assert owner.is_system_admin is True
        assert verify_password(" test-only-owner-password ", owner.password_hash)
        assert not verify_password("test-only-owner-password", owner.password_hash)
        assert db.query(Organization).count() == 1


@pytest.mark.parametrize("configured", [False, True])
def test_existing_user_is_not_modified_or_promoted(database, monkeypatch, configured):
    with database() as db:
        org = Organization(name="Existing team", plan="free")
        db.add(org)
        db.flush()
        db.add(User(email="member@example.com", password_hash="existing-hash",
                    organization_id=org.id, role="member", is_system_admin=False))
        db.commit()
    if configured:
        monkeypatch.setenv("ADMIN_EMAIL", "member@example.com")
        monkeypatch.setenv("ADMIN_PASSWORD", "replacement-test-password")

    seed.seed_admin_user()

    with database() as db:
        member = db.query(User).one()
        assert member.role == "member"
        assert member.is_system_admin is False
        assert member.password_hash == "existing-hash"
        assert db.query(Organization).one().name == "Existing team"


def test_failed_bootstrap_does_not_leave_an_orphan_organization(database, monkeypatch):
    monkeypatch.setenv("ADMIN_EMAIL", "owner@example.com")
    monkeypatch.setenv("ADMIN_PASSWORD", "test-only-password")

    def failed_hash(_password):
        raise RuntimeError("test hashing failure")

    monkeypatch.setattr(seed, "hash_password", failed_hash)
    with pytest.raises(RuntimeError, match="test hashing failure"):
        seed.seed_admin_user()

    with database() as db:
        assert db.query(User).count() == 0
        assert db.query(Organization).count() == 0
