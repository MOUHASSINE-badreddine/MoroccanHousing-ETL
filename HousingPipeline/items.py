# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HousingpipelineItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Surface=scrapy.Field()
    Prix=scrapy.Field()
    Nombre_Chambres=scrapy.Field()
    Ville=scrapy.Field()
    Secteur=scrapy.Field()
    Etage=scrapy.Field()
    Salons=scrapy.Field()
    Meuble=scrapy.Field()
    Equipements=scrapy.Field()
    pass
