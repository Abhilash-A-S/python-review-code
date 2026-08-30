import secrets
from dataclasses import dataclass, field
from pathlib import Path

import yaml
from sqlalchemy import text


@dataclass
class Basket:
    items: list[str] = field(default_factory=list)


def same_identifier(actual_id: int, requested_id: int) -> bool:
    return actual_id == requested_id


def parse_integer(value: str) -> int | None:
    try:
        return int(value)
    except ValueError:
        return None


def create_token() -> str:
    return secrets.token_urlsafe(32)


def parse_settings(payload: str) -> object:
    return yaml.safe_load(payload)


def read_export(export_root: Path, filename: str) -> str:
    root = export_root.resolve()
    candidate = (root / filename).resolve()
    if not candidate.is_relative_to(root):
        raise ValueError("export path escapes configured root")
    return candidate.read_text(encoding="utf-8")


def find_account(session, email: str):
    return session.execute(
        text("SELECT * FROM accounts WHERE email=:email"), {"email": email}
    ).first()
