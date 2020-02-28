from .brand import BrandRepository
from .category import CategoryRepository, CategorySpecRepository
from .product import SkuDetailRepository, SkuRepository, SpuRepository
from .store import StoreRepository

brand_repo = BrandRepository()
category_repo = CategoryRepository()
category_spec_repo = CategorySpecRepository()
store_repo = StoreRepository()
spu_repo = SpuRepository()
sku_repo = SkuRepository()
sku_detail_repo = SkuDetailRepository()
