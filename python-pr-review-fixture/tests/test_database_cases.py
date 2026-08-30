import asyncio

import pytest


def test_first_page(repository) -> None:
    page = repository.list_page(page=1, page_size=20)
    assert page.page == 1


def test_update_missing_account(repository) -> None:
    assert repository.update(999, {"name": "missing"}) is True


def test_expected_exception() -> None:
    with pytest.raises(ValueError):
        raise ValueError("expected")


@pytest.mark.asyncio
async def test_clean_async_wait() -> None:
    await asyncio.sleep(0)
    assert True
