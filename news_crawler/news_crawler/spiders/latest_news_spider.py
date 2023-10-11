import scrapy
from ..items import LatestNewsItem

class LatestNewsSpider(scrapy.Spider):
    name = 'latestnewsspider'
    allowed_domains = ["cybersecuritynews.com"]
    start_urls = ['https://cybersecuritynews.com/']

    def parse(self, response):
        # Loop through the article links and follow them
        # This was until on 2023.11.10: '/html/body/div[6]/div[2]/div[2]//a/@href'
        for article_link in response.xpath('/html/body/div[6]/div[2]/div/div/div/div[3]/div/div[1]//a/@href').extract():
            yield response.follow(article_link, callback=self.parse_article)

    def parse_article(self, response):
        # Extract article data
        article = LatestNewsItem()
        article['id'] = response.url.split('/')[-2]  # Article ID / string! from URL - unique?
        article['title'] = response.xpath('/html/head/title/text()').get()
        article['body'] = response.xpath('/html/body').get()
        # article['content'] = response.xpath("//div[@class='td-ss-main-content'][1]").get() -- TODO

        yield article
