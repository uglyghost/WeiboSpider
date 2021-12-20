#!/usr/bin/env python
# encoding: utf-8

import re

from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from items import RelationshipItem
import time
from bson import ObjectId
from pymongo import MongoClient

user = 'weibo'
pwd = '123456'
host = '127.0.0.1'
port = '27017'
db_name = 'weibo_senior'

uri = "mongodb://%s:%s@%s" % (user, pwd, host + ":" + port + "/" + db_name)

client = MongoClient(uri)
mongodb = client.weibo

class FollowerSpider(Spider):

    def __init__(self, id_list=None):
        self.id_list = id_list

    name = "follower_spider"
    base_url = "https://weibo.cn"

    def start_requests(self):

        # query = {"_id": ObjectId("618557946f63bdf1e4ac1523")}

        for value in self.id_list:
            # print(value)
            user_ids = [value]
            # mongodb['tmp'].update_one(query, {"$set": {"follow_id": value}})
            # user_ids = ['1087770692', '1699432410', '1266321801']
            urls = [f"{self.base_url}/{user_id}/follow?page=1" for user_id in user_ids]
            for url in urls:
                yield Request(url, callback=self.parse)

    def parse(self, response):
        if response.url.endswith('page=1'):
            all_page = re.search(r'/>&nbsp;1/(\d+)页</div>', response.text)
            if all_page:
                all_page = all_page.group(1)
                all_page = int(all_page)
                for page_num in range(2, all_page + 1):
                    page_url = response.url.replace('page=1', 'page={}'.format(page_num))
                    yield Request(page_url, self.parse, dont_filter=True, meta=response.meta)
        selector = Selector(response)
        urls = selector.xpath('//a[text()="关注他" or text()="关注她" or text()="取消关注"]/@href').extract()
        uids = re.findall('uid=(\d+)', ";".join(urls), re.S)
        ID = re.findall('(\d+)/follow', response.url)[0]
        for uid in uids:
            relationships_item = RelationshipItem()
            relationships_item['crawl_time'] = int(time.time())
            relationships_item["fan_id"] = ID
            relationships_item["followed_id"] = uid
            relationships_item["_id"] = ID + '-' + uid
            yield relationships_item
