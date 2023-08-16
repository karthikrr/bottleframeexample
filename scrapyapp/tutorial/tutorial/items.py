# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst, Join
from w3lib.html import remove_tags


class ProductItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor= Join())
    description = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor= Join())
    upc = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor= Join())
    product_url = scrapy.Field()
    image_url = scrapy.Field()
