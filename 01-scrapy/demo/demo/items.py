import scrapy


class Page(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    desc = scrapy.Field()
    links = scrapy.Field()
