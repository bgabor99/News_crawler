# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsCrwalerItem(scrapy.Item):
    id = scrapy.Field()
    domain = scrapy.Field()
    title = scrapy.Field()
    body = scrapy.Field()
    content = scrapy.Field()
    author = scrapy.Field()
    date = scrapy.Field()
