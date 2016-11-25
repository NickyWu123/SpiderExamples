# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy





class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    rate=scrapy.Field()
    fivestar=scrapy.Field()
    fourstar=scrapy.Field()
    threestar=scrapy.Field()
    twostar=scrapy.Field()
    onestar=scrapy.Field()
    index=scrapy.Field()

