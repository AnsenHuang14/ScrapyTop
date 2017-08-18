# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ToplistItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	PkgName = scrapy.Field()
	Title = scrapy.Field()
	genre = scrapy.Field()
	numDownloads = scrapy.Field()
	fileSize =  scrapy.Field()
	Lan = scrapy.Field()
	Country = scrapy.Field()
	operatingSystems = scrapy.Field()
	LogoUrl = scrapy.Field()
	ClkUrl = scrapy.Field()
	pass
