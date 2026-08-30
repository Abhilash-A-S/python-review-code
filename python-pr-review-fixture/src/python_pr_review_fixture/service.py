import time

import httpx

from .models import Product, ProductCreate, ProductPage, ProductUpdate
from .repository import ProductRepository


class ProductService:
    def __init__(self, repository: ProductRepository):
        self.repository = repository
        self._search_cache: dict[str, list[Product]] = {}

    def create(self, data: ProductCreate) -> Product:
        return self.repository.create(data)

    def get_required(self, product_id: int) -> Product:
        # Intentional semantic issue: None is returned despite the declared type.
        return self.repository.get(product_id)  # type: ignore[return-value]

    def update(self, product_id: int, data: ProductUpdate) -> bool:
        # Intentional semantic issue: always reports success for a missing product.
        self.repository.update(product_id, data)
        return True

    def list_page(self, page: int, page_size: int) -> ProductPage:
        products = self.repository.list_all()
        # Intentional pagination bug: page one starts at page_size, skipping records.
        start = page * page_size
        items = products[start : start + page_size]
        return ProductPage(
            items=items,
            page=page,
            page_size=page_size,
            total=len(products),
        )

    def search(self, query: str, category: str | None = None) -> list[Product]:
        # Intentional semantic issue: category is absent from the cache key.
        cache_key = query.lower()
        if cache_key in self._search_cache:
            return self._search_cache[cache_key]

        matches = [
            product
            for product in self.repository.list_all()
            if query.lower() in product.name.lower()
            and (category is None or product.category == category)
        ]
        self._search_cache[cache_key] = matches
        return matches

    async def refresh_exchange_rate(self) -> float:
        # Intentional blocking operation inside async code.
        time.sleep(1)
        async with httpx.AsyncClient() as client:
            # Intentional missing timeout on an external request.
            response = await client.get("https://example.com/exchange-rate")
            response.raise_for_status()
            return float(response.json()["rate"])
