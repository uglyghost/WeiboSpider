# -*- coding: utf-8 -*-
import pymongo
from pymongo.errors import DuplicateKeyError
from settings import MONGO_HOST, MONGO_PORT


class MongoDBPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
        db = client['weibo']
        self.Users = db["Users"]
        self.Tweets = db["Tweets"]
        self.Comments = db["Comments"]
        self.Relationships = db["Relationships"]
        self.Reposts = db["Reposts"]

    def process_item(self, item, spider):
        if spider.name == 'comment_spider':
            self.insert_item(self.Comments, item)
        elif spider.name == 'fan_spider':
            self.insert_item(self.Relationships, item)
        elif spider.name == 'follower_spider':
            self.insert_item(self.Relationships, item)
        elif spider.name == 'user_spider':
            self.insert_item(self.Users, item)
        elif spider.name == 'tweet_spider':
            self.insert_item_tweet(self.Tweets, item)
        elif spider.name == 'repost_spider':
            self.insert_item(self.Reposts, item)
        return item

    @staticmethod
    def insert_item_tweet(collection, item):
        try:
            collection.insert(dict(item))
        except DuplicateKeyError:
            pass

    @staticmethod
    def insert_item(collection, item):
        try:

            query = {"_id": item["_id"]}

            # 重复检查，看是否存在数据
            count = collection.count_documents(query)
            # print(tmp_dict)

            if count == 0:
                # 不存在，添加
                collection.insert(dict(item))
            # collection.insert(dict(item))
        except DuplicateKeyError:
            pass

