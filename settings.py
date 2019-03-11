# -*- coding: utf-8 -*-

# Scrapy settings for carhome project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'carhome'

SPIDER_MODULES = ['carhome.spiders']
NEWSPIDER_MODULE = 'carhome.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'carhome (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#     'Accept-Language': 'zh-CN,zh;q=0.9',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
#     'Cache-Control': 'max-age=0',
#     'Connection': 'keep-alive',
#     'Cookie': '__ah_uuid=D3821C85-BC2C-43AC-9AE4-DDDABA3ECD82; fvlid=1550806553341TPQZTD3OzY; sessionip=111.201.209.39; sessionid=4A4F73AB-655C-4A2E-AC4F-DC63FC201B4F%7C%7C2019-02-22+11%3A35%3A24.307%7C%7Cwww.baidu.com; area=110105; ahpau=1; sessionuid=4A4F73AB-655C-4A2E-AC4F-DC63FC201B4F%7C%7C2019-02-22+11%3A35%3A24.307%7C%7Cwww.baidu.com; Hm_lvt_9924a05a5a75caf05dbbfb51af638b07=1550806602; ahsids=4764; sessionvid=17DFE442-84ED-4B61-877E-B5113B5BD52D; wwwjbtab=0%2C0; pvidchain=100833; ahpvno=72; Hm_lpvt_9924a05a5a75caf05dbbfb51af638b07=1550827300; ref=www.baidu.com%7C0%7C0%7C0%7C2019-02-22+17%3A21%3A10.318%7C2019-02-22+11%3A35%3A24.307',
#     'Host': 'car.autohome.com.cn',
#     'Referer': 'https://car.autohome.com.cn/price/list-0_5-0-0-0-0-0-0-0-0-0-0-0-0-0-0-2.html',
#     'Upgrade-Insecure-Requests': '1',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'carhome.middlewares.CarhomeSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'carhome.middlewares.SeleniumMiddleware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'carhome.pipelines.MongoPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

MAX_PAGE = 20

MONGO_URI = 'localhost'
MONGO_DB = 'carhome'