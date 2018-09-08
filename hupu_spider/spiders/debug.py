from scrapy.cmdline import execute
import os, sys
from time import sleep
from multiprocessing import Pool

sys.path.append(os.path.dirname(__file__))


def run_spider(number):
    print('spider %s is started...' % number)
    execute('scrapy runspider hupu_user.py'.split(' '))


if __name__ == '__main__':
    p = Pool(20)
    for i in range(20):
        p.apply_async(run_spider, args=(i,))
        sleep(1)
    p.close()
    p.join()