# from scrapy.http import Request
import scrapy
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from demo.items import Page


class WikipediaSpider(scrapy.Spider):
    name = "wikipedia"
    allowed_domains = ["it.wikipedia.org"]
    start_urls = [
        "http://it.wikipedia.org/wiki/Premio_Nobel",
        "http://it.wikipedia.org/wiki/Premio_Nobel_per_la_pace",
        "http://it.wikipedia.org/wiki/Premio_Nobel_per_la_letteratura",
        "http://it.wikipedia.org/wiki/Premio_Nobel_per_la_fisica",
        "http://it.wikipedia.org/wiki/Premio_Nobel_per_la_chimica",
        "http://it.wikipedia.org/wiki/Premio_Nobel_per_l%27economia"
    ]

    extractor = SgmlLinkExtractor()

    def filter_link(self, link):
        if not link.url.startswith("http://it.wikipedia.org"):
            return False

        for badchar in '?#=':
            if badchar in link.url:
                return False
        return True

    def simplify(self, link):
        return {
            'url': link.url,
            'text': link.text,
        }

    def parse(self, response):
        sel = Selector(response)

        item = Page()
        item['url'] = response.url
        item['title'] = ' '.join(sel.xpath('//title/text()').extract())
        item['desc'] = ' '.join(sel.xpath('.//p//text()').extract())
        item['links'] = map(self.simplify,
                            filter(self.filter_link,
                                   self.extractor.extract_links(response)))
        yield item

        #for item in item['links']:
        #    yield Request(url=item['url'])
