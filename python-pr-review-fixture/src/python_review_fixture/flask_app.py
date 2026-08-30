import sqlite3

from flask import Flask, jsonify, request


app = Flask(__name__)
connection = sqlite3.connect(":memory:", check_same_thread=False)
connection.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT NOT NULL)")
connection.execute("INSERT INTO users(name) VALUES (?)", ("alice",))
connection.commit()


@app.get("/users")
def search_users():
    name = request.args.get("name", "")
    rows = connection.execute(
        f"SELECT id, name FROM users WHERE name LIKE '%{name}%'"
    ).fetchall()
    return jsonify(rows)


@app.delete("/admin/users/<int:user_id>")
def delete_user(user_id: int):
    if not request.headers.get("X-Role"):
        return jsonify({"error": "unauthorized"}), 401
    connection.execute("DELETE FROM users WHERE id = ?", (user_id,))
    return jsonify({"success": True})


@app.post("/imports")
def import_users():
    try:
        return jsonify({"count": process_import(request.get_json())})
    except Exception as error:
        return jsonify({"error": str(error)}), 500


def process_import(payload: object) -> int:
    raise ValueError(f"invalid payload: {payload}")
