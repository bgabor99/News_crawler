import scrapy
import psycopg2
from ..items import NewsCrawlerItem

class NewsSpider(scrapy.Spider):
    name = 'newsspider'
    start_urls = ['https://cybersecuritynews.com/']

    def parse(self, response):
        # Loop through the article links and follow them
        for article_link in response.xpath('/html/body/div[6]/div[2]/div/div/div/div[3]/div/div[1]//a/@href').extract(): # loop for each latest article link TODO
            yield response.follow(article_link, callback=self.parse_article)

    def parse_article(self, response):
        # Extract article data
        article = NewsCrawlerItem()
        article['id'] = response.url.split('/')[-2]  # Article ID / string! from URL - unique?
        # article['title'] = response.css('h1::text').get()
        # article['content'] = ' '.join(response.css('p::text').extract())

        print("MyArticle: ", article['id'])

        # Save article data to PostgreSQL # TODO
        yield article

