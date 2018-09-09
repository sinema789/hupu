# from scrapy.cmdline import execute
# import os, sys
# from time import sleep
# from multiprocessing import Pool
#
# sys.path.append(os.path.dirname(__file__))
#
#
# def run_spider(number):
#     print('spider %s is started...' % number)
#     execute('scrapy crawl hupu_user'.split(' '))
#
#
# if __name__ == '__main__':
#     p = Pool(5)
#     for i in range(5):
#         p.apply_async(run_spider, args=(i,))
#         sleep(1)
#     p.close()
#     p.join()