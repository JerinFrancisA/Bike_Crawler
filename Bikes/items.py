import scrapy


class BikesItem(scrapy.Item):

    item_name = scrapy.Field()
    item_url = scrapy.Field()
    item_price = scrapy.Field()

