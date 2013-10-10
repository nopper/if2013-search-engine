from scrapy.http import Request
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

from demo.items import Page

class WikiSpider(BaseSpider):
    name = "wikispider"
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
        hxs = HtmlXPathSelector(response)

        item = Page()
        item['url'] = response.url
        item['title'] = ' '.join(hxs.select('//title/text()').extract())
        item['desc'] = ' '.join(hxs.select('.//p//text()').extract())
        item['links'] = map(self.simplify,
                            filter(self.filter_link,
                                   self.extractor.extract_links(response)))
        yield item

        #for item in item['links']:
        #    yield Request(url=item['url'])

