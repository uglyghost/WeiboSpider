# -*- coding: utf-8 -*-

BOT_NAME = 'spider'

SPIDER_MODULES = ['spiders']
NEWSPIDER_MODULE = 'spiders'

ROBOTSTXT_OBEY = False

# change cookie to yours
#DEFAULT_REQUEST_HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
#    'Cookie': '_T_WM=da71ffa6f7f128ab6e63ff072db80606; SUB=_2A25MgTTBDeRhGeNM6VcX-SrJzjuIHXVvilyJrDV6PUJbkdCOLVTYkW1NTiDEuIdSD9l1__cJQlNUYbZ4BsuX91QV; SCF=ArQVOs0FURqY19hrE2SGFtDk0PfOPJD71jGtPZEhGoMerq3Jyz0ms7PhXAicNQP5JhFT0hT_ob82BdBsVsFhPqQ.'}

#DEFAULT_REQUEST_HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
#    'Cookie': '_T_WM=da71ffa6f7f128ab6e63ff072db80606; WEIBOCN_WM=3349; H5_wentry=H5; backURL=https://passport.sina.cn/; SCF=AttQRDsHb-v6zLir9qtBBIcTXn7d8govOhlAKcT5G1UlfGLJhNrUUBoiFaKjAC6uuVuYVfXwsVdGZ_VtZvnix3U.; SUB=_2A25MgY_MDeRhGeFJ6lsU-S3Fyz6IHXVvjRGErDV6PUJbktB-LW-hkW1NfG6bOCX7HXjOi2Gx6DFCp9WcM_KeXwm5; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5oMQfn.VKjspLb_QEWee-55NHD95QNS024SK.01K5EWs4Dqcjbi--NiK.Xi-2Ri--ciKnRi-zNSo2NeKq01hnfe8Yp1Kn41Btt; SSOLoginState=1636171676'}

DEFAULT_REQUEST_HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'Cookie': '_T_WM=da71ffa6f7f128ab6e63ff072db80606; SUB=_2A25MgTTBDeRhGeNM6VcX-SrJzjuIHXVvilyJrDV6PUJbkdCOLVTYkW1NTiDEuIdSD9l1__cJQlNUYbZ4BsuX91QV; SCF=ArQVOs0FURqY19hrE2SGFtDk0PfOPJD71jGtPZEhGoMerq3Jyz0ms7PhXAicNQP5JhFT0hT_ob82BdBsVsFhPqQ.'}

CONCURRENT_REQUESTS = 16

DOWNLOAD_DELAY = 1

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