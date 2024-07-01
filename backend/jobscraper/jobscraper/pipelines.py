# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2


class JobscraperPipeline:
    def process_item(self, item, spider):
        return item

class SaveToPostgresPipeline:
    def __init__(self):
        self.connection = psycopg2.connect(
            dbname='your_database',
            user='your_user',
            password='your_password',
            host='db',  # This should match the service name in docker-compose
            port=5432
        )
        self.cursor = self.connection.cursor()
