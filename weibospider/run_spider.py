#!/usr/bin/env python
# encoding: utf-8

import os
import sys
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from spiders.tweet import TweetSpider
from spiders.comment import CommentSpider
from spiders.follower import FollowerSpider
from spiders.user import UserSpider
from spiders.fan import FanSpider
from spiders.repost import RepostSpider
from bson import ObjectId
from pymongo import MongoClient

user = 'weibo'
pwd = '123456'
host = '127.0.0.1'
port = '27017'
db_name = 'weibo'

uri = "mongodb://%s:%s@%s" % (user, pwd, host + ":" + port + "/" + db_name)

client = MongoClient(uri)
mongodb = client.weibo

if __name__ == '__main__':
    mode = sys.argv[1]
    os.environ['SCRAPY_SETTINGS_MODULE'] = f'settings'
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    mode_to_spider = {
        'comment': CommentSpider,
        'fan': FanSpider,
        'follow': FollowerSpider,
        'tweet': TweetSpider,
        'user': UserSpider,
        'repost': RepostSpider,
    }
    list1 = mongodb['Relationships'].find().distinct("fan_id")
    if mode == "user":
        list2 = mongodb['uid_list'].find().distinct("uid")
        # list2 = mongodb['Users'].find().distinct("_id")
    elif mode == "fan":
        # list2 = mongodb['Relationships'].find().distinct("follow_id")
        list2 = mongodb['uid_list'].find().distinct("uid")
    elif mode == "follow":
        list2 = mongodb['Users'].find().distinct("_id")
        # list2 = mongodb['User'].find()
    elif mode == "tweet":
        list2 = mongodb['tweet'].find().distinct("user_id")

    # diff_list = list(set(list1) - set(list2))
    diff_list = list2

    # print(len(diff_list))
    # print(diff_list)

    # diff_list = ['1193491727', '1900093290', '5726715057', '2683882661', '1880143303']

    # 调用进程池的map_async()方法，接收一个函数(爬虫函数)和一个列表(用户ID)
    # 官方网站标准库文档里边map_async用法如下：p.may_async(func,[1,2,3])
    # 函数会依次取出列表的每个元素作为参数来执行func(1), func(2), func(3)
    process.crawl(mode_to_spider[mode], diff_list)
    # the script will block here until the crawling is finished
    process.start()