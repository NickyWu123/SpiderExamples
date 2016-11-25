# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule
import sys
sys.stdout=open('output.txt','w')
class JinshuComSpider(CrawlSpider):
    name = "jianshu_spider"
    allowed_domains = ["jianshu.com"]
    start_urls = ['http://www.jianshu.com/']


    rules = [
        Rule(LinkExtractor(allow=(r'http://www.jianshu.com/users/[a-z0-9]+?'))),
        Rule(LinkExtractor(allow=(r'http://www.jianshu.com/p/[a-z0-9]+?')), callback="parse_item")
        ]



    def parse_item(self, response):
       	with open('output.txt','a+') as file:
           	file.write(str(response.url)+'\n') 
