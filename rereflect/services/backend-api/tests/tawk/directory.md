# tawk.to regression checks

`conftest.py` mounts the actual integration, source and webhook routers with real authentication and an isolated database. It avoids unrelated native SAML imports. `test_ingestion.py` covers encrypted configuration, tenant boundaries, signatures, visitor-only normalization, retries, broker failure, disconnect and PostgreSQL concurrency.

Run from backend-api: `../../.venv/bin/python -m pytest --confcutdir=tests/tawk tests/tawk -q`. Set `TAWK_TEST_DATABASE_URL` privately for PostgreSQL; the fixture creates and removes only a uniquely named test schema.
