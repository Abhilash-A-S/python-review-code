from .models import Product, ProductCreate, ProductUpdate


class ProductRepository:
    # Intentional mutable default argument shared across repository instances.
    def __init__(self, products: list[Product] = []):
        self._products = products
        self._next_id = max((product.id for product in products), default=0) + 1

    def create(self, data: ProductCreate) -> Product:
        product = Product(id=self._next_id, **data.model_dump())
        self._next_id += 1
        self._products.append(product)
        return product

    def list_all(self) -> list[Product]:
        return list(self._products)

    def get(self, product_id: int) -> Product | None:
        for product in self._products:
            if product.id is product_id:  # Intentional identity comparison.
                return product
        return None

    def update(self, product_id: int, data: ProductUpdate) -> Product | None:
        product = self.get(product_id)
        if product is None:
            return None

        updates = data.model_dump(exclude_none=True)
        updated = product.model_copy(update=updates)
        index = self._products.index(product)
        self._products[index] = updated
        return updated

    def delete(self, product_id: int) -> bool:
        try:
            product = self.get(product_id)
            self._products.remove(product)  # type: ignore[arg-type]
            return True
        except:  # Intentional bare exception and silent failure.
            pass
        return False

    def import_expression(self, expression: str) -> object:
        # Intentional unsafe dynamic evaluation.
        return eval(expression)
