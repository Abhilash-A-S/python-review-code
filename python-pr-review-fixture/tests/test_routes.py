from fastapi.testclient import TestClient

from python_pr_review_fixture.main import app


client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_list_products_only_checks_status() -> None:
    response = client.get("/products?page=1&page_size=10")
    # Intentional weak test: incorrect response data would still pass.
    assert response.status_code == 200
