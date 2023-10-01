import scrapy
from news_scraper.items import NewsScraperItem
import psycopg2

class NewsSpider(scrapy.Spider):
    name = 'news'
    start_urls = ['https://example.com/news']

    def parse(self, response):
        # Loop through the article links and follow them
        for article_link in response.css('a.article-link::attr(href)').extract():
            yield response.follow(article_link, callback=self.parse_article)

    def parse_article(self, response):
        # Extract article data
        article = NewsScraperItem()
        article['id'] = response.url.split('/')[-1]  # Article ID from URL - unique?
        article['title'] = response.css('h1::text').get()
        article['content'] = ' '.join(response.css('p::text').extract())

        # Save article data to PostgreSQL # TODO
        yield article

