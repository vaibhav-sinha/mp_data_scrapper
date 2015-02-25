# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MpDataScrapperItem(scrapy.Item):
    name = scrapy.Field()
    constituency = scrapy.Field()
    party = scrapy.Field()
    father = scrapy.Field()
    mother = scrapy.Field()
    dob = scrapy.Field()
    birth_place = scrapy.Field()
    marital_status = scrapy.Field()
    spouse_name = scrapy.Field()
    num_sons = scrapy.Field()
    num_daughters = scrapy.Field()
    state = scrapy.Field()
    permanent_address = scrapy.Field()
    present_address = scrapy.Field()
    email = scrapy.Field()
    education = scrapy.Field()
    positions_held = scrapy.Field()
    social_cultural_activities = scrapy.Field()
    sports_clubs = scrapy.Field()
    pastimes_recreation = scrapy.Field()
    countries_visited = scrapy.Field()
    other_info = scrapy.Field()
    photo = scrapy.Field()
