import scrapy
from ..items import NewsCrwalerItem
import logging

class LatestNewsSpider(scrapy.Spider):
    name = 'latestnewsspider'
    allowed_domains = ["cybersecuritynews.com"]
    start_urls = ['https://cybersecuritynews.com/']

    def parse(self, response):
        logger = logging.getLogger(f'Spider - {self.name}')
        logger.info('Spider parse started')
        # Loop through the article links and follow them
        for article_link in response.xpath('/html/body/div[6]/div[2]/div/div/div/div[3]/div/div[1]//a/@href').extract():
            yield response.follow(article_link, callback=self.parse_article)

    def parse_article(self, response):
        # Extract article data
        article = NewsCrwalerItem()
        article['id'] = response.url.split('/')[-2]  # Article ID
        article['domain'] = (','.join(self.allowed_domains))
        article['title'] = response.xpath('/html/head/title/text()').get()
        article['body'] = response.xpath('/html/body').get()
        article['content'] = response.xpath("/div[@class='td-ss-main-content'][1]").get()
        article['author'] = response.xpath("//header//a[contains(@href, 'author')]/text()[1]").get()
        article['date'] = response.xpath('//header//time[@datetime]/@datetime[1]').get()

        yield article
