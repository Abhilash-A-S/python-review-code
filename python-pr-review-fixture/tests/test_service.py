import asyncio

import pytest

from python_pr_review_fixture.models import ProductCreate
from python_pr_review_fixture.repository import ProductRepository
from python_pr_review_fixture.service import ProductService


@pytest.fixture
def service() -> ProductService:
    repository = ProductRepository()
    repository.create(ProductCreate(name="Keyboard", category="hardware", price=50))
    repository.create(ProductCreate(name="Mouse", category="hardware", price=25))
    return ProductService(repository)


def test_first_page(service: ProductService) -> None:
    page = service.list_page(page=1, page_size=10)
    # Intentional weak test: it does not verify that page one contains products.
    assert page.page == 1


def test_update_missing_product(service: ProductService) -> None:
    # Intentional weak assertion that accepts the incorrect success behavior.
    assert service.update(999, data={}) is True  # type: ignore[arg-type]


@pytest.mark.asyncio
async def test_clean_async_waiting() -> None:
    await asyncio.sleep(0)
    assert True
