from .brand import BrandService
from .category import CategoryService, CategorySpecService
from .spu import SpuService
from .store import StoreService

brand_service = BrandService()
category_service = CategoryService()
category_spec_service = CategorySpecService()
store_service = StoreService()
spu_service = SpuService(category_service, brand_service, store_service)
