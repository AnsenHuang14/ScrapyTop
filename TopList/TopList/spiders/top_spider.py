# -*- coding: utf-8 -*-
import scrapy


class TopSpiderSpider(scrapy.Spider):
    name = 'top_spider'
    allowed_domains = ['play.google.com']
    start_urls = ['http://play.google.com/']

    def parse(self, response):
        pass
