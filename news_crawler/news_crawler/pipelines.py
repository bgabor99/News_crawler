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


class NewsCrawlerPipeline:

    def __init__(self):
        print("HOST", DATABASES['default']['NAME'])
        # Connect to database
        self.connection = psycopg2.connect(host=DATABASES['default']['HOST'], user=DATABASES['default']['USER'], password=DATABASES['default']['PASSWORD'], dbname=DATABASES['default']['NAME'])
        # Create cursor
        self.cursor = self.connection.cursor()


    def process_item(self, item, spider):
        dt = datetime.now(timezone.utc)
        insert_to_article ="""INSERT INTO news_crawler.article ("Article_ID", "Processed_Date", "Article_Body") values (%s,%s,%s)"""
        article_data = (str(item["id"]), dt, str(item["body"]))
        insert_to_latest_news ="""INSERT INTO news_crawler."Latest_news" ("Article_ID", "Title") values (%s,%s)"""
        latest_news_data = (str(item["id"]), str(item["title"]))
        try:
            self.cursor.execute(insert_to_article, article_data)
            self.cursor.execute(insert_to_latest_news, latest_news_data)
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            raise DropItem(f"Item could not be inserted: {e}")

        ## Commit
        self.connection.commit()
        return item
    
    def close_spider(self, spider):
        # Close cursor and connection to database 
        self.cursor.close()
        self.connection.close()
