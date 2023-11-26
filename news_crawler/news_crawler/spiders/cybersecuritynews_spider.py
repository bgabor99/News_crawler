import scrapy
from ..items import NewsCrawlerItem
import logging
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor


class CyberSecurityNewsSpider(CrawlSpider):
    name = "cybersecuritynewsspider"
    allowed_domains = ["cybersecuritynews.com"]
    start_urls = ["https://cybersecuritynews.com"]

    rules = (
        # Extract and follow all links!
        Rule(LxmlLinkExtractor(
            unique=True,
            deny=[
                r'author',
                r'\?amp',
                r'\?noamp',
                r'tag',
                r'author',
                r'\?=',
                r'\?s=',
                r'filter',
                r'page'
            ]
            ),
            callback='parse_item',
            follow=True),
    )

    def parse_item(self, response):
        logger = logging.getLogger(f'Spider - {self.name}')
        logger.info('Spider parse started')
        logger.info(f'Crawl {response.url} page')

        # Extract article data
        article = NewsCrawlerItem()
        article['id'] = \
            response.url.split(self.start_urls[0], 1)[1]  # Page ID
        article['domain'] = \
            (','.join(self.allowed_domains))
        article['title'] = \
            response.xpath('/html/head/title/text()').get()
        article['body'] = \
            response.xpath('/html/body').get()
        article['content'] = \
            response.xpath(
                "//div[contains(@class, 'td-post-content')][1]"
            ).get()
        article['author'] = \
            response.xpath(
                "//header//a[contains(@href, 'author')]/text()[1]"
            ).get()
        article['date'] = \
            response.xpath('//header//time[@datetime]/text()[1]').get()

        yield article
