import re

import scrapy
from dateutil import parser

from ..items import WikiTableItem


class WikiTableSpider(scrapy.Spider):
    name = 'wiki-table'

    def start_requests(self):
        """
        Init url from command
        :return:
        """
        urls = [getattr(self, 'url', '')]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """
        Parse info then collect to raw data
        :param response: scrapy response after call a URL
        :return: dict
        """
        item = WikiTableItem()

        rs = []
        num_item = len(response.xpath('//*[@id="mw-content-text"]/div[1]/table/tbody/tr'))
        for num in range(2, num_item + 1):
            row = self.parse_row(
                response.xpath('//*[@id="mw-content-text"]/div[1]/table/tbody/tr[{num}]/td'
                               .format(num=num))
            )
            rs.append(row)
        item['data'] = rs
        item['page_title'] = response.xpath('/html/head/title//text()').extract_first()
        yield item

    def parse_row(self, row):
        return {
            'mark': re.findall(r'\d+\.\d+', ' '.join(row[0].xpath('text()').extract_first()).replace(" ", ""))[0],
            'athlete': ' '.join(row[1].xpath('text()').extract()).strip(),
            'date': parser.parse(' '.join(row[2].xpath('text()').extract()).strip()),
            'venue': ' '.join(row[3].xpath('text()').extract()).strip()
        }
