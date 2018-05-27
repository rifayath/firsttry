# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MytryItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    page_heading = scrapy.Field()
    page_title = scrapy.Field()
    page_link = scrapy.Field()
    page_content = scrapy.Field()
    page_content_block = scrapy.Field()

    image_url = scrapy.Field()
    images = scrapy.Field()
    
