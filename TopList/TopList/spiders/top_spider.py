# -*- coding: utf-8 -*-
from TopList.items import ToplistItem
import scrapy

def read_url(path=''):
    start_urls = list()
    with open(path, 'rb') as f:
        start_urls.append(f.read())
    start_urls = start_urls[0].split('\n')
    return start_urls

class TopSpiderSpider(scrapy.Spider):
    name = 'top_spider'
    allowed_domains = ['play.google.com']
    
    def __init__(self,path, *args,**kwargs):
        super(TopSpiderSpider, self).__init__(*args, **kwargs)
        self.start_urls = read_url(path)

    def parse(self, response):
    	app = ToplistItem()
    	app['PkgName'] = response.url.split('=')[1].replace('&hl','')
        app['Title'] = response.xpath('//div[@class="id-app-title"]/text()')[0].extract()
        app['genre'] = response.xpath('//span[@itemprop="genre"]/text()')[0].extract()
        app['numDownloads'] = response.xpath('//div[@itemprop="numDownloads"]/text()')[0].extract()
        if len(response.xpath('//div[@itemprop="fileSize"]/text()'))>0:
        	app['fileSize'] =  response.xpath('//div[@itemprop="fileSize"]/text()')[0].extract()
        else:
        	app['fileSize'] = " "
        app['Lan'] =  response.url.split('=')[2]
        app['Country'] =  response.url.split('=')[2]
        app['operatingSystems'] = response.xpath('//div[@itemprop="operatingSystems"]/text()')[0].extract().replace(' ','')
        app['LogoUrl'] =  response.xpath('//img[@class="cover-image"]//@src')[0].extract()
        app['ClkUrl'] =  response.url
        # print app['PkgName'],app['Title'],app['genre'],app['numDownloads'],app['fileSize']
        # print  app['Lan'],app['Country'],app['operatingSystems'],app['LogoUrl'],app['ClkUrl']
        yield app