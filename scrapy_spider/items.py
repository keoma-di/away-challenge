# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WikiTableItem(scrapy.Item):
    data = scrapy.Field()
    page_title = scrapy.Field()
