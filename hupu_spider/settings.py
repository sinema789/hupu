# -*- coding: utf-8 -*-

# Scrapy settings for hupu_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'hupu_spider'

SPIDER_MODULES = ['hupu_spider.spiders']
NEWSPIDER_MODULE = 'hupu_spider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'hupu_spider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'hupu_spider.middlewares.HupuSpiderSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'hupu_spider.middlewares.CookieMiddleware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'hupu_spider.pipelines.AddressPipeline': 300,
    'hupu_spider.pipelines.MongoPipeline': 301
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'

COOKIE = "_cnzz_CV30020080=buzi_cookie%7C26e6d9a0.26a7.3922.a1c1.9cc539d7cf32%7C-1; _dacevid3=26e6d9a0.26a7.3922.a1c1.9cc539d7cf32; __gads=ID=ba0d0c5f9bee6684:T=1535442381:S=ALNI_MYV93WG5cte_QP4jrjaXeL9jwctQA; _HUPUSSOID=fcf4291d-500d-476c-aa90-2ded1feb2039; _CLT=918ebe7bb324d8673460f7af1d701a5c; AUM=dgyXw1slR58LjeuoFFtrj3DHjN5nt-yqlWtWpTno5j7lw; PHPSESSID=svcppr71pm795aun878sv6m8b0; _cnzz_CV30020080=buzi_cookie%7C26e6d9a0.26a7.3922.a1c1.9cc539d7cf32%7C-1; u=29692677|56CW5Zyo5omL6Lef5oiR6LWw5Li2|cb06|bbc02eca257c4f28178b4ebee9965f92|257c4f28178b4ebe|aHVwdV9lNDExMjQzMTliZDE1NTgx; us=309b03516c1194bcc9243ceb52d3c6f63ef2075e47a07b789d8cedf554862ea1cc50ac084e63513418f0e4e1dab7ac6bc83696574e4764483a2f51cf1e50ad69; ua=19695122; __dacevst=90c039b3.2f11c544|1536224780473"

# scrapy-redis 配置
# 1. 设置请求调度器采用 scrapy-redis 实现方案
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 2. 设置过滤类，实现去重功能
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 3. 配置redis连接信息
REDIS_URL = "redis://@106.12.209.201:6379/1"
# 4. 配置持久化
SCHEDULER_PERSIST = True

# 配置mongodb连接信息
MONGO_URI = '106.12.209.201:27017'
MONGO_DATABASE = 'hupu01'
