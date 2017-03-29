import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from event.items import EventItem


# scrapy crawl kktix -o kktix.csv -t csv

class KKtixSpider(scrapy.Spider):
    name = 'kktix'
    def start_requests(self):
        for url in ['https://kktix.com/events?category_id=&end_at=2016%2F12%2F31&page=' + str(i) + '&search=&start_at=2016%2F01%2F01&utf8=%E2%9C%93' for i in range(1, 500)]:
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        urls = response.xpath('//li[contains(concat(" ", @class, " "), " clearfix ")]/h2/a/@href').extract()
        cates = response.xpath('//li[contains(concat(" ", @class, " "), " clearfix ")]/*[contains(concat(" ", @class, " "), " category ")]/text()').extract()
        dates = response.xpath('//li[contains(concat(" ", @class, " "), " clearfix ")]/*[contains(concat(" ", @class, " "), " date ")]/*[contains(concat(" ", @class, " "), " timezoneSuffix ")]/text()').extract()
        for url, cate, date in zip(urls, cates, dates):
            item = EventItem()
            item['category'] = cate
            item['date'] = date[:-7]
            yield scrapy.Request(url, callback=self.parse_event, meta={'item': item})
            
    def parse_event(self, response):
        item = response.meta['item']
        if len(response.xpath('//*[contains(concat(" ", @class, " "), " content ")]/*[contains(concat(" ", @class, " "), " header ")]/*[contains(concat(" ", @class, " "), " header-title ")]/h1/text()').extract()) > 0:
            item['title'] = response.xpath('//*[contains(concat(" ", @class, " "), " content ")]/*[contains(concat(" ", @class, " "), " header ")]/*[contains(concat(" ", @class, " "), " header-title ")]/h1/text()').extract()
        else:
            item['title'] = response.css('div.header-title > h1::text').extract()
        if len(response.xpath('//*[contains(concat(" ", @class, " "), " info ")]/li[2]/*[contains(concat(" ", @class, " "), " info-desc ")]/text()').extract()) > 0:
                    item['address'] = response.xpath('//*[contains(concat(" ", @class, " "), " info ")]/li[2]/*[contains(concat(" ", @class, " "), " info-desc ")]/text()').extract()
        else:
            item['address'] = response.css('span.address::text').extract()
        # print(item['cate'], item['addr'])
        yield item
    