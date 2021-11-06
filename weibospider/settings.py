# -*- coding: utf-8 -*-

BOT_NAME = 'spider'

SPIDER_MODULES = ['spiders']
NEWSPIDER_MODULE = 'spiders'

ROBOTSTXT_OBEY = False

# change cookie to yours
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'Cookie': '_T_WM=da71ffa6f7f128ab6e63ff072db80606; SUB=_2A25MgTTBDeRhGeNM6VcX-SrJzjuIHXVvilyJrDV6PUJbkdCOLVTYkW1NTiDEuIdSD9l1__cJQlNUYbZ4BsuX91QV; SCF=ArQVOs0FURqY19hrE2SGFtDk0PfOPJD71jGtPZEhGoMerq3Jyz0ms7PhXAicNQP5JhFT0hT_ob82BdBsVsFhPqQ.; SSOLoginState=1636123793'}

CONCURRENT_REQUESTS = 16

DOWNLOAD_DELAY = 3

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': None,
    'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': None,
    'middlewares.IPProxyMiddleware': 100,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 101,
}

ITEM_PIPELINES = {
    'pipelines.MongoDBPipeline': 300,
}

MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017
