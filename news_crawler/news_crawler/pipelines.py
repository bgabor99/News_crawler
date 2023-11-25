# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2
from datetime import datetime, timezone
from news_crawler.settings import DATABASES
from scrapy.exceptions import DropItem
import logging


class NewsCrawlerPipeline:

    def __init__(self):
        # Connect to database and create cursor
        self.connection = psycopg2.connect(
            host=DATABASES['default']['HOST'],
            user=DATABASES['default']['USER'],
            password=DATABASES['default']['PASSWORD'],
            dbname=DATABASES['default']['NAME']
        )
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        used_spiders = ['cybersecuritynewsspider', 'thehackernewsspider']
        if (spider.name in used_spiders):
            item = self.process_news_item(item)

        return item

    def check_if_article_id_exists(self, item):
        article_id = str(item["domain"]) + str(item["id"])
        query = """SELECT * FROM news_crawler.article
                WHERE article."Article_ID" = (%s)"""
        data = (article_id,)
        self.cursor.execute(query, data)
        return self.cursor.fetchall()

    def process_news_item(self, item):
        try:
            dt = datetime.now(timezone.utc)
            article_id = str(item["domain"]) + str(item["id"])
            # Check if its already in the database
            result = self.check_if_article_id_exists(item)
            if result:
                logging.info("Item already in exists in the database \
                             with this Article_ID: %s" % article_id)
            else:
                insert_to_article = """INSERT INTO news_crawler.article \
                                    ("Article_ID",
                                    "Domain",
                                    "Processed_Date")
                                    values (%s,%s,%s)"""
                article_data = (article_id,
                                str(item["domain"]),
                                dt)
                insert_to_common = """INSERT INTO news_crawler."common"
                                    ("Article_ID", "Title",
                                    "Body", "Content", "Author", "Date")
                                    values (%s,%s,%s,%s,%s,%s)"""
                common_data = (article_id,
                               str(item["title"]),
                               str(item["body"]),
                               str(item["content"]),
                               str(item["author"]),
                               str(item["date"]))
                try:
                    self.cursor.execute(insert_to_article, article_data)
                    self.cursor.execute(insert_to_common, common_data)
                    self.connection.commit()
                    logging.info(
                        "Article inserted into "
                        "database with Article_ID: %s" % article_id
                        )
                except Exception as e:
                    self.connection.rollback()
                    logging.warning(
                        "Dropped item "
                        "because this error occured:: %s" % e
                        )
                    raise DropItem(f"Item could not be inserted: {e}")
        except Exception as e:
            self.connection.rollback()
            logging.warning("Dropped item because this error occured:: %s" % e)
            raise DropItem(f"Item could not be selected: {e}")

        return item

    def close_spider(self, spider):
        # Close cursor and connection to database
        self.cursor.close()
        self.connection.close()
