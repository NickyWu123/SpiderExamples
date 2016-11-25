# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys
import redis
reload(sys)
sys.setdefaultencoding( "utf-8" )

class DoubanPipeline(object):
    def process_item(self, item, spider):
        r=redis.Redis(host='127.0.0.1',port=6379,password='test')
        r.hsetnx(item['title'],'rate',item['rate'])
        r.hsetnx(item['title'],'fivestar',item['fivestar'])
        r.hsetnx(item['title'],'fourstar',item['fourstar'])
        r.hsetnx(item['title'],'threestar',item['threestar'])
        r.hsetnx(item['title'],'twostar',item['twostar'])
        r.hsetnx(item['title'],'onestar',item['onestar'])

