# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2
from urllib.parse import urlparse


class JobscraperPipeline:
    def process_item(self, item, spider):
        return item

class SaveToPostgresPipeline:
    def __init__(self):
        DATABASE_URL = 'postgresql://postgres:password@db/myapi'
        result = urlparse(DATABASE_URL)
        
        self.connection = psycopg2.connect(
            dbname=result.path[1:],  # Exclude the leading '/'
            user=result.username,
            password=result.password,
            host=result.hostname,
            port=result.port
        )
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        
        try:
            # Check if the organization exists
            self.cursor.execute(
                """
                SELECT id FROM organizations WHERE name = %s
                """,
                (adapter.get('organization_name'),)
            )
            organization = self.cursor.fetchone()
            
            if organization:
                organization_id = organization[0]
            else:
                # Insert the organization if it doesn't exist
                self.cursor.execute(
                    """
                    INSERT INTO organizations (name)
                    VALUES (%s)
                    RETURNING id
                    """,
                    (adapter.get('organization_name'),)
                )
                organization_id = self.cursor.fetchone()[0]

            # Insert the job with the organization_id
            self.cursor.execute(
                """
                INSERT INTO jobs (job_title, organization_id, location, grade, occupational_groups, closing_date, job_description) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    adapter.get('job_title'),
                    organization_id,
                    adapter.get('location'),
                    adapter.get('grade'),
                    adapter.get('occupational_groups'),
                    adapter.get('closing_date'),
                    adapter.get('job_description')
                )
            )
            self.connection.commit()
        except psycopg2.Error as e:
            self.connection.rollback()  # Rollback the transaction on error
            spider.logger.error(f"Error inserting item: {e}")
        
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.connection.close()