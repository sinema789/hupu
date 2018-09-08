# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class CookieMiddleware(object):

    def __init__(self):
        self.cookie = '_dacevid3=26e6d9a0.26a7.3922.a1c1.9cc539d7cf32; __gads=ID=ba0d0c5f9bee6684:T=1535442381:S=ALNI_MYV93WG5cte_QP4jrjaXeL9jwctQA; _HUPUSSOID=fcf4291d-500d-476c-aa90-2ded1feb2039; _CLT=918ebe7bb324d8673460f7af1d701a5c; AUM=dgyXw1slR58LjeuoFFtrj3DHjN5nt-yqlWtWpTno5j7lw; PHPSESSID=svcppr71pm795aun878sv6m8b0; _cnzz_CV30020080=buzi_cookie%7C26e6d9a0.26a7.3922.a1c1.9cc539d7cf32%7C-1; u=29692677|56CW5Zyo5omL6Lef5oiR6LWw5Li2|cb06|bbc02eca257c4f28178b4ebee9965f92|257c4f28178b4ebe|aHVwdV9lNDExMjQzMTliZDE1NTgx; us=1322187576585e8ccad9cf81b90f89963ef2075e47a07b789d8cedf554862ea1cc50ac084e63513418f0e4e1dab7ac6bc6cde701885b187a1e1da46b198e70db; ua=19695244; __dacevst=f2cf54a6.0cd7a8e1|1536230851511'

    def process_request(self, request, spider):
        request.cookies = dict(map(lambda x: x.split('=', 1), self.cookie.split('; ')))


class HupuSpiderSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class HupuSpiderDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
