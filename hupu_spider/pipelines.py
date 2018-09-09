# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from hupu_spider.items import HupuSpiderItem


class AddressPipeline(object):

    def process_item(self, item, spider):

        addresses = [
            '北京市', '天津市', '河北省', '山西省', '内蒙古', '辽宁省', '吉林省', '黑龙江', '上海市', '江苏省', '浙江省', '安徽省',
            '福建省', '江西省', '山东省', '河南省', '湖北省', '湖南省', '广东省', '广西省', '海南省', '重庆市', '四川省', '贵州省',
            '云南省', '西藏', '陕西省', '甘肃省', '青海省', '宁夏', '新疆', '香港', '澳门', '台湾省'
        ]
        if item.get('address') is not None and item.get('address') not in addresses:
            item['address'] = "海外"

        return item


class MongoPipeline(object):

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        self.db[HupuSpiderItem.collection].create_index([('uid', pymongo.ASCENDING)])

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if isinstance(item, HupuSpiderItem):
            self.db[item.collection].update({'uid': item.get('uid')}, {'$set': item}, True)

        return item
