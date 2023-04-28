# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 11:26:32 2023


"""

import scrapy
from practicalone.items import PracticaloneItem

#create a class
class ThirdSpider(scrapy.Spider):
    #create a name
    name = "Books3"
    #get urls
    start_urls = [
        "https://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html",
        "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
        "https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html",
        "https://books.toscrape.com/catalogue/soumission_998/index.html",
        ]
   
    #define
    def parse(self, response):
        item = PracticaloneItem()
        item['title'] = response.xpath("//div[@class='col-sm-6 product_main']/h1/text()").get()
        price_text = response.xpath("//p[@class='price_color']/text()").get()
        item['price'] = float(price_text.replace('£', '').replace('\xa0', '').strip())
        item['category'] = response.xpath("//ul[@class='breadcrumb']/li[3]/a/text()").get()
        item['in_stock'] = response.xpath("normalize-space(//p[@class='instock availability']/i/following::node()[1])").get()
      
        
        
        return item
        
    
    
    
    
    
