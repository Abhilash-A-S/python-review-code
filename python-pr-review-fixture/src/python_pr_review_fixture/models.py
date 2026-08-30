from pydantic import BaseModel, Field


class ProductCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    category: str = Field(min_length=1, max_length=50)
    price: float = Field(gt=0)
    tags: list[str] = Field(default_factory=list)


class ProductUpdate(BaseModel):
    name: str | None = None
    category: str | None = None
    price: float | None = Field(default=None, gt=0)
    tags: list[str] | None = None


class Product(ProductCreate):
    id: int


class ProductPage(BaseModel):
    items: list[Product]
    page: int
    page_size: int
    total: int
