"""交互信息相关的常量"""

# Global Exceptions Message
SERVER_LOG_ERROR = 'SERVER ERROR'
SERVER_UI_ERROR = 'SERVER ERROR, PLEASE CONTACT THE MANAGER'
NOT_FOUND_ERROR = '404 NOT FOUND'
RECORD_NOT_FOUND_ERROR = 'RECORD NOT FOUND'

# Extensions/Providers Message
MINIO_CONFIG_ERROR = (
    'Either MINIO_ENDPOINT or MINIO_ACCESS_KEY or MINIO_SECRET_KEY needs to be set.'
)
REDIS_CONNECT_ERROR = 'Redis连接异常，程序退出'


# Product Service Message
CATEGORY_NOT_EXIST = '所选分类不存在'
BRAND_NOT_EXIST = '所选品牌不存在'
STORE_NOT_EXIST = '所选商铺不存在'
