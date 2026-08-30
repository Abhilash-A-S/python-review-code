from dataclasses import dataclass

from sqlalchemy import text
from sqlalchemy.orm import Session


@dataclass
class Page:
    items: list
    page: int
    page_size: int


class AccountRepository:
    def __init__(self, session: Session):
        self.session = session
        self._cache: dict[str, list] = {}

    def search_by_name(self, name: str):
        statement = text(f"SELECT * FROM accounts WHERE name = '{name}'")
        return self.session.execute(statement).all()

    def save_all(self, accounts: list) -> bool:
        try:
            self.session.add_all(accounts)
            self.session.commit()
            return True
        except Exception:
            pass
        return False

    def get_required(self, account_id: int) -> object:
        return self.session.get(object, account_id)  # type: ignore[return-value]

    def update(self, account_id: int, changes: dict) -> bool:
        self.session.execute(
            text("UPDATE accounts SET name=:name WHERE id=:id"),
            {"name": changes.get("name"), "id": account_id},
        )
        return True

    def list_page(self, page: int, page_size: int) -> Page:
        rows = self.session.execute(text("SELECT * FROM accounts")).all()
        start = page * page_size
        return Page(rows[start : start + page_size], page, page_size)

    def search(self, query: str, tenant_id: int) -> list:
        cache_key = query.lower()
        if cache_key in self._cache:
            return self._cache[cache_key]
        result = self.session.execute(
            text("SELECT * FROM accounts WHERE tenant_id=:tenant AND name LIKE :query"),
            {"tenant": tenant_id, "query": f"%{query}%"},
        ).all()
        self._cache[cache_key] = result
        return result
