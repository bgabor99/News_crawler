from ..items import PageCrawlerItem
import logging
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor


class InputPageSpider(CrawlSpider):
    name = "inputpagespider"
    allowed_domains = []
    start_urls = []

    def __init__(self, *a, **kw):
        self.rules = (
            # Extract and follow all links!
            Rule(LxmlLinkExtractor(
                unique=True,
                deny=[]
                ),
                callback='parse_item',
                follow=True),
        )
        super(InputPageSpider, self).__init__(*a, **kw)
        logger = logging.getLogger(f'Spider - {self.name}')
        try:
            file_name = 'domains_input.txt'
            logger.info(f'Opening {file_name} file')
            with open(file_name,'r') as file:
                for line in file:
                    self.allowed_domains.append(line)
                    self.start_urls.append('http://%s' % line)  ## Adding HTTP prefix for start URLs
            logger.info(f'{file_name} opened successfully')
            logger.info(f'Allowed domains from the {file_name} are these: {self.allowed_domains}')
            logger.info(f'Start URLs form the {file_name} are these: {self.start_urls}')
        except FileNotFoundError as e:
            logger.error(f'File not found error: {e}')
        except Exception as e:
            logger.error(f'File error: {e}')

    def parse_item(self, response):
        logger = logging.getLogger(f'Spider - {self.name}')
        logger.info('Spider parse started')
        logger.info(f'Crawl {response.url} page')

        # Process page data
        page = PageCrawlerItem()
        page['id'] = \
            response.request.url  # Page ID
        page['domain'] = (','.join(self.allowed_domains))
        page['page'] = response.body

        yield page
