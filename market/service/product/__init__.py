from .brand import BrandService
from .category import CategoryService
from .sku import SkuService
from .spec import SpecService
from .spu import SpuService
from .store import StoreService

brand_service = BrandService()
category_service = CategoryService()
spec_service = SpecService()
store_service = StoreService()
spu_service = SpuService(category_service, brand_service, store_service)
sku_service = SkuService()
