import scrapy
from ..items import NewsCrawlerItem
import logging
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor


class ThaHackerNewsSpider(CrawlSpider):
    name = "thehackernewsspider"
    allowed_domains = ["thehackernews.com"]
    start_urls = ["https://thehackernews.com"]

    rules = (
        # Extract and follow all links!
        Rule(LxmlLinkExtractor(
            unique=True,
            deny=[
                r'search',
                r'sales',
                r'page',
                r'images'
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
            response.url.split(self.allowed_domains[0], 1)[1]  # Article ID
        article['domain'] = \
            (','.join(self.allowed_domains))
        article['title'] = \
            response.xpath('/html/head/title/text()').get()
        article['body'] = \
            response.xpath('/html/body').get()
        article['content'] = \
            response.xpath(
                "//div[contains(@class, 'articlebody')][1]"
            ).get()
        article['author'] = \
            response.xpath(
                "//span[@class='p-author']//i[1]"
            ).get()
        article['date'] = \
            response.xpath("//span[@class='p-author']//i[2]").get()

        yield article
