from scrapy.item import Item, Field

class Page(Item):
    title = Field()
    url = Field()
    desc = Field()
    links = Field()

