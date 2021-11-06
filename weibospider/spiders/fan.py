#!/usr/bin/env python
# encoding: utf-8

import re
from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from items import RelationshipItem
import time
from pymongo import MongoClient
from bson import ObjectId
import pandas as pd

user = 'weibo'
pwd = '123456'
host = '127.0.0.1'
port = '27017'
db_name = 'weibo'

uri = "mongodb://%s:%s@%s" % (user, pwd, host + ":" + port + "/" + db_name)

client = MongoClient(uri)
mongodb = client.weibo

class FanSpider(Spider):
    name = "fan_spider"
    base_url = "https://weibo.cn"

    def start_requests(self):
        query = {"_id": ObjectId("618557946f63bdf1e4ac1523")}
        # 重复检查，看是否存在数据
        count = mongodb['tmp'].find_one(query)
        user_id = count['fan_id']
        tmp = mongodb['Relationships'].find().distinct("fan_id")

        countA = []
        lock = 0
        for document in tmp:
            if document == user_id:
                lock = 1

            if lock == 1:
                countA.append(document)

        for value in countA:
            user_ids = [value]
            mongodb['tmp'].update_one(query, {"$set": {"fan_id": value}})
            # user_ids = ['1087770692', '1699432410', '1266321801']
            urls = [f"{self.base_url}/{user_id}/fans?page=1" for user_id in user_ids]
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
        urls = selector.xpath('//a[text()="关注他" or text()="关注她" or text()="移除"]/@href').extract()
        uids = re.findall('uid=(\d+)', ";".join(urls), re.S)
        ID = re.findall('(\d+)/fans', response.url)[0]
        for uid in uids:
            relationships_item = RelationshipItem()
            relationships_item['crawl_time'] = int(time.time())
            relationships_item["fan_id"] = uid
            relationships_item["followed_id"] = ID
            relationships_item["_id"] = 'fans' + '-' + uid + '-' + ID
            yield relationships_item
