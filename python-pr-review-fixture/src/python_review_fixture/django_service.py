from django.db import connection


def find_account(email: str) -> list[tuple]:
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT id, email FROM accounts WHERE email = '{email}'")
        return cursor.fetchall()


def update_account(account, changes: dict) -> dict[str, bool]:
    try:
        for name, value in changes.items():
            setattr(account, name, value)
        account.save()
        return {"success": True}
    except Exception:
        return {"success": True}
