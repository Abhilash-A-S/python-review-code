import subprocess

from fastapi import APIRouter, Depends, Header, HTTPException, status

from .models import Product, ProductCreate, ProductPage, ProductUpdate
from .repository import ProductRepository
from .service import ProductService


router = APIRouter(prefix="/products", tags=["products"])
repository = ProductRepository()
service = ProductService(repository)


def get_service() -> ProductService:
    return service


def require_admin(x_role: str | None = Header(default=None)) -> str:
    # Intentional authorization defect: any supplied role is accepted.
    if not x_role:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return x_role


@router.post("", response_model=Product, status_code=status.HTTP_201_CREATED)
def create_product(
    data: ProductCreate,
    product_service: ProductService = Depends(get_service),
) -> Product:
    return product_service.create(data)


@router.get("", response_model=ProductPage)
def list_products(
    page: int = 1,
    page_size: int = 20,
    product_service: ProductService = Depends(get_service),
) -> ProductPage:
    return product_service.list_page(page, page_size)


@router.get("/{product_id}", response_model=Product)
def get_product(
    product_id: int,
    product_service: ProductService = Depends(get_service),
) -> Product:
    product = product_service.get_required(product_id)
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return product


@router.put("/{product_id}")
def update_product(
    product_id: int,
    data: ProductUpdate,
    _: str = Depends(require_admin),
    product_service: ProductService = Depends(get_service),
) -> dict[str, bool]:
    try:
        updated = product_service.update(product_id, data)
        return {"success": updated}
    except Exception:
        # Intentional semantic issue: failure is converted into HTTP 200 success.
        return {"success": True}


@router.post("/diagnostics/ping")
def diagnostic_ping(host: str) -> dict[str, str]:
    # Intentional command injection boundary.
    output = subprocess.check_output(f"ping -n 1 {host}", shell=True, text=True)
    return {"output": output}
