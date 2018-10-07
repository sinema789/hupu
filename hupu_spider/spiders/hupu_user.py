# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
import sys
from scrapy_redis.spiders import RedisCrawlSpider
from hupu_spider.items import HupuSpiderItem


class HupuUserSpider(RedisCrawlSpider):
    print(sys.path)
    name = 'hupu_user'
    allowed_domains = ['hupu.com']
    start_url = ['https://my.hupu.com/zhangjiawei', 'https://my.hupu.com/91700603242537',
                 'https://my.hupu.com/176192780288726', 'https://my.hupu.com/linshuhao',
                 'https://my.hupu.com/Tracy_Mcgrady', 'https://my.hupu.com/7963307555404',
                 'https://my.hupu.com/SmithKobe', 'https://my.hupu.com/194086995549379']
    redis_key = "hupu_user:start_urls"

    rules = (
        Rule(LinkExtractor(restrict_xpaths=('//div[@id="following"]/p/a',)), follow=True),
        Rule(LinkExtractor(restrict_xpaths=('//div[@class="search_user_list index_bbs"]/ul/li//a[@class="u"]',)),
             callback='parse_item', follow=False),
        Rule(LinkExtractor(restrict_xpaths=('//a[@class="next"]',)), follow=True)
    )

    def parse_item(self, response):
        item = HupuSpiderItem()
        # 用户名
        name = response.xpath('//div[@itemprop="name"]/text()').extract_first()
        # uid
        uid = response.xpath('//img[@id="j_head"]/@uid').extract_first()
        # 性别
        gender = response.xpath('//span[@itemprop="gender"]/text()').extract_first()
        # 所在地
        address = response.xpath('//span[@itemprop="address"]/text()').extract_first()
        # 主队
        team = response.xpath('//span[@itemprop="affiliation"]/a/text()').extract_first()
        # 声望
        prestige_pattern = re.compile(r'社区声望：<.*?>(.*?)<br>?', re.S)
        try:
            prestige = int(re.findall(prestige_pattern, response.text)[0].strip())
            item['prestige'] = prestige
        except (IndexError, ValueError):
            print('数据出错')
        if response.url == 'https://my.hupu.com/39275947968908':
            item['prestige'] = response.xpath('//span[text()="社区声望："]/following-sibling::*[1]/text()').extract_first()

        # 等级
        level_pattern = re.compile(r'社区等级：<.*?>(.*?)<br>?', re.S)
        try:
            level = int(re.findall(level_pattern, response.text)[0].strip())
            item['level'] = level
        except IndexError:
            print('数据出错')
        # 在线时间
        online_time_pattern = re.compile(r'在线时间：<.*?>(.*?)<br>?', re.S)
        try:
            online_time = int(re.findall(online_time_pattern, response.text)[0].strip().replace('小时', ''))
            item['online_time'] = online_time
        except IndexError:
            print('数据出错')
            item['online_time'] = 0
        # 加入时间
        join_date_pattern = re.compile(r'加入时间：<.*?>(.*?)<br>?', re.S)
        try:
            join_date = int(re.findall(join_date_pattern, response.text)[0].strip().split('-')[0])
            item['join_date'] = join_date
        except IndexError:
            print('数据出错')

        # 判断字段是否存在
        if gender is not None:
            item['gender'] = gender
        else:
            item['gender'] = '无'

        if address is not None:
            if address[::2].strip() in ['西藏', '宁夏', '新疆', '香港', '澳门']:
                item['address'] = address[:2].strip()
            else:
                item['address'] = address[:3].strip()

        if team is not None:
            item['team'] = team

        if name is not None:
            item['name'] = name
        if uid is not None:
            item['uid'] = int(uid)

        yield item
