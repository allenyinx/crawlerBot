# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AirgentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


# 产品
class ProductItem(scrapy.Item):
    gp_icon = scrapy.Field()  # 图标
    gp_name = scrapy.Field()  # GP名称


# 评论
class GPReviewItem(scrapy.Item):
    avatar_url = scrapy.Field()  # 头像链接
    user_name = scrapy.Field()  # 用户名称