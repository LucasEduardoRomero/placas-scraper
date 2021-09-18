# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PlacasScraperItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    produto = scrapy.Field()
    preco = scrapy.Field()
    numr_de_fotos = scrapy.Field()
    url_img = scrapy.Field()
    datahora_pub = scrapy.Field()