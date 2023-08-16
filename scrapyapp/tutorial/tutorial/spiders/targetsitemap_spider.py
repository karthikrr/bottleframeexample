'''
This sitemap is extended from sitemap spider
'''
import scrapy
from scrapy.spiders import SitemapSpider
from tutorial.items import ProductItem
from scrapy.loader import ItemLoader

class TargetSpider(SitemapSpider):
    name = 'targetspider'
    sitemap_urls = ['https://www.target.com/sitemap_pdp-index.xml.gz']
    sitemap_rules = [('/p/', "parse_product")]
    sitemap_follow = ['/pdp/']

    def parse_product(self, response):
        # Using item loaders 
        l = ItemLoader(item=ProductItem(),response=response)
        l.add_xpath('name', '//h1[@id="pdp-product-title-id"]')
        l.add_xpath('description', '//*[@id="specAndDescript"]/div[1]/div[2]/div[1]')
        l.add_xpath('upc', '//div[@data-test="item-details-specifications"]/div/b[contains(text(),"UPC")]/parent::div')
        l.add_value('product_url', response.url)
        l.add_xpath('image_url', '//*[@id="pageBodyContainer"]/div/div[1]/div[2]/div[1]/div/section/div[2]/div[1]/div/button[1]/div/div/div/div/img/@src')
        return l.load_item()
        # yield {
        #     "url":response.url
        # }