# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class JobItem(scrapy.Item):
    job_title = scrapy.Field()
    organization = scrapy.Field()
    location = scrapy.Field()
    grade = scrapy.Field()
    occupational_groups = scrapy.Field()
    closing_date = scrapy.Field()
    job_description = scrapy.Field()
