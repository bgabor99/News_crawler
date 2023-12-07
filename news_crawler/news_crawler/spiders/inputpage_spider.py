import asyncio
from ..items import PageCrawlerItem
import logging
from scrapy.http import Request
from scrapy.spiders import Spider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.utils.project import get_project_settings


class InputPageSpider(Spider):
    name = "inputpagespider"
    # allowed_domains = ["people.inf.elte.hu"]
    # start_urls = ["https://people.inf.elte.hu/eoxdzj/beadando"]
    allowed_domains = []
    start_urls = []


    def start_requests(self):
        print("START REQUEST")
        self.rules = (
            # Extract and follow all links!
            Rule(LxmlLinkExtractor(
                unique=True,
                deny=[]
                ),
                callback='parse_item',
                follow=True),
        )

        logger = logging.getLogger(f'Spider - {self.name}')
        print('TRY OPEN')
        
        try:
            file_name = 'domains_input.txt'
            logger.info(f'Opening {file_name} file')
            with open(file_name, 'r') as file:
                for line in file:
                    domain, url = line.strip().split(' ')
                    # Create a request object to crawl the URL
                    request = Request(url, callback=self.parse)
                    request.meta["domain"] = domain
                    
                    yield request
            logger.info(f'{file_name} opened successfully')
            logger.info(f'Allowed domains from {file_name} are these: {self.allowed_domains}')
            logger.info(f'Start URLs from {file_name} are these: {self.start_urls}')
        except FileNotFoundError as e:
            logger.error(f'File not found error: {e}')
        except Exception as e:
            logger.error(f'File error: {e}')
        
        

    def parse(self, response):
        print('PARSE')
        logger = logging.getLogger(f'Spider - {self.name}')
        logger.info('Spider parse started')
        logger.info(f'Crawl {response.url} page')

        full_url = response.request.url
        request = Request(full_url, callback=self.parse)
        request.meta["domain"] = response.meta["domain"]
        '''
        # Process page data
        page = PageCrawlerItem()
        page['id'] = \
            response.request.url  # Page ID
        page['domain'] = (','.join(self.allowed_domains))
        page['page'] = response.body
        '''

        # yield page
        yield request
