import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

from python_review_fixture.database_cases import AccountRepository


@pytest.fixture
def repository():
    engine = create_engine("sqlite+pysqlite:///:memory:")
    with engine.begin() as connection:
        connection.execute(
            text("CREATE TABLE accounts (id INTEGER PRIMARY KEY, name TEXT, tenant_id INTEGER)")
        )
        connection.execute(
            text("INSERT INTO accounts(name, tenant_id) VALUES ('alice', 1), ('bob', 1)")
        )
    with Session(engine) as session:
        yield AccountRepository(session)
