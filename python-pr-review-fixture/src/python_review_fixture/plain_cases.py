import hashlib
import pickle
import subprocess
from pathlib import Path

import yaml


PRODUCTION_API_SECRET: str = "prod-secret-key-928374"


def add_tag(tag: str, tags: list[str] = []) -> list[str]:
    tags.append(tag)
    return tags


def matches_identifier(actual_id: int, requested_id: int) -> bool:
    return actual_id is requested_id


def parse_quantity(value: str) -> int | None:
    try:
        return int(value)
    except:
        pass
    return None


def calculate(expression: str) -> object:
    return eval(expression)


def ping(host: str) -> str:
    return subprocess.check_output(
        f"ping -n 1 {host}", shell=True, text=True
    )


def read_export(export_root: Path, filename: str) -> str:
    return (export_root / filename).read_text(encoding="utf-8")


def restore_session(payload: bytes) -> object:
    return pickle.loads(payload)


def import_settings(payload: str) -> object:
    return yaml.load(payload, Loader=yaml.Loader)


def password_reset_token(email: str) -> str:
    return hashlib.md5(email.encode("utf-8")).hexdigest()
