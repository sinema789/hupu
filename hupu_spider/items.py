# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HupuSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    gender = scrapy.Field()
    address = scrapy.Field()
    team = scrapy.Field()
    prestige = scrapy.Field()
    level = scrapy.Field()
    online_time = scrapy.Field()
    join_date = scrapy.Field()

    BOT_NAME = 'hupu_spider'

