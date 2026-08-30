from python_review_fixture.flask_app import app


def test_search_users_only_checks_status() -> None:
    response = app.test_client().get("/users?name=alice")
    assert response.status_code == 200


def test_complete_error_response() -> None:
    response = app.test_client().post("/imports", json={"invalid": True})
    assert response.status_code == 500
    assert "error" in response.get_json()
