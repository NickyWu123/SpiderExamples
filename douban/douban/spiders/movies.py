# -*- coding: utf-8 -*-
import scrapy
import urllib
import json
from scrapy.http.request import Request
from douban.items import DoubanItem
class MoviesSpider(scrapy.Spider):
    name = "movies"
    allowed_domains = ["douban.com"]
    params={'type':'movie','tag':'豆瓣高分','sort':'recommend','page_limit':20}
    start_urls=[]
    for i in range(0,50,20):
        params['page_start']=i
        url='https://movie.douban.com/j/search_subjects?'
        url=url + urllib.urlencode(params)
        start_urls.append(url)
    def parse(self, response):
        data=json.loads(response.body)
        for index,i in enumerate(data['subjects']):
            yield Request(i['url'],callback=self.per_movie,meta={'title':i['title'],'rate':i['rate'],'index':index})

    def per_movie(self,response):
        item=DoubanItem()
        item['title']=response.meta["title"]
        item['rate']=response.meta["rate"]
        item['index']=response.meta["index"]
        ratioes=response.xpath('//*[@id="interest_sectl"]/div[1]/span/text()').extract()
        for index,ratio in enumerate(ratioes):
            if index==1:
                  item['fivestar']=ratioes[index]
            if index==3:
                  item['fourstar']=ratioes[index]
            if index==5:
                  item['threestar']=ratioes[index]
            if index==7:
                  item['twostar']=ratioes[index]
            if index==9:
                  item['onestar']=ratioes[index]
        yield item

