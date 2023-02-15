# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from services.graph import line_plot


class ScrapySpiderPipeline(object):
    def __init__(self):
        pass

    def process_item(self, item, spider):
        """
        This method is called for every item pipeline component.
        Bind data to vertical axis and horizontal axis
        """
        x = []
        y = []
        for data in item['data']:
            x.append(data['date'])
            y.append(data['mark'])
        line_plot(x, y, item['page_title'])
        return item
