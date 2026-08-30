import pytest

from python_pr_review_fixture.models import ProductCreate
from python_pr_review_fixture.repository import ProductRepository


def test_create_and_get_product() -> None:
    repository = ProductRepository()
    created = repository.create(
        ProductCreate(name="Keyboard", category="hardware", price=50)
    )

    assert repository.get(created.id) == created


def test_missing_product_returns_none() -> None:
    repository = ProductRepository()
    assert repository.get(999) is None


def test_delete_missing_product_returns_false() -> None:
    repository = ProductRepository()
    assert repository.delete(999) is False


def test_clean_exception_assertion() -> None:
    with pytest.raises(ZeroDivisionError):
        _ = 1 / 0
