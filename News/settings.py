# -*- coding: utf-8 -*-

# Scrapy settings for News project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

DEBUG = False

BOT_NAME = 'News'

SPIDER_MODULES = ['News.spiders']
NEWSPIDER_MODULE = 'News.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'News (+http://www.yourdomain.com)'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS=32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN=16
#CONCURRENT_REQUESTS_PER_IP=16

# Disable cookies (enabled by default)
#COOKIES_ENABLED=False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED=False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'News.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': None,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'News.middlewares.RotateUserAgentMiddleware': 405,
}

DOWNLOAD_HANDLERS = {'s3': None}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.telnet.TelnetConsole': None,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
#AUTOTHROTTLE_ENABLED=True
# The initial download delay
#AUTOTHROTTLE_START_DELAY=5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY=60
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG=False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED=True
#HTTPCACHE_EXPIRATION_SECS=0
#HTTPCACHE_DIR='httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES=[]
#HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage'

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html

if DEBUG:
    ITEM_PIPELINES = {
        "News.pipelines.CompatiblePipeline": 300,
        "News.pipelines.CleanPipeline": 301,
        "News.pipelines.CachePipeline": 302,
        "News.pipelines.StartMetaPipeline": 313,
        "News.pipelines.MonitorPipeline": 314,
        "News.pipelines.PrintPipeline": 315,
    }
    LOG_LEVEL = "INFO"
    REDIS_URL = 'redis://localhost:6379'
    POSTGRES = "postgresql://postgres:lee@localhost/test"
    MONGO_URI = "mongodb://localhost:27017"
    MONGO_DATABASE = "test"
    MONGO_COLLECTION = "news"
else:
    ITEM_PIPELINES = {
        "News.pipelines.CompatiblePipeline": 300,
        "News.pipelines.CleanPipeline": 301,
        "News.pipelines.CachePipeline": 302,
        "News.pipelines.StartMetaPipeline": 313,
        "News.pipelines.MonitorPipeline": 314,
        'News.pipelines.StorePipeline': 315,
    }
    LOG_LEVEL = "INFO"
    REDIS_URL = 'redis://ccd827d637514872:LYcache2015@ccd827d637514872.m.cnhza.kvstore.aliyuncs.com:6379'
    # POSTGRES = "postgresql://postgres:ly@postgres&2015@120.27.163.25/BDP"
    MONGO_URI = "mongodb://h44:27017,h213:27017,h241:27017/?replicaSet=myset"
    MONGO_DATABASE = "news_ver2"
    MONGO_COLLECTION = "NewsItems"

