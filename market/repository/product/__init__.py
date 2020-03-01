from .brand import BrandRepository
from .category import CategoryRepository
from .product import SkuDetailRepository, SkuRepository, SpuRepository
from .spec import SpecRepository
from .store import StoreRepository

brand_repo = BrandRepository()
category_repo = CategoryRepository()
spec_repo = SpecRepository()
store_repo = StoreRepository()
spu_repo = SpuRepository()
sku_repo = SkuRepository()
sku_detail_repo = SkuDetailRepository()
