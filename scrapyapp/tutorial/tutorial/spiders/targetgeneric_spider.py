'''
This sitemap is extended from sitemap spider
'''
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from tutorial.items import ProductItem
from scrapy.loader import ItemLoader
import re

class CostcoGenericSpider(CrawlSpider):
    name = 'costcocategoryspider'
    # allowed_domains = ["https://www.flipkart.com/"]
    # start_urls = ['https://www.flipkart.com/audio-video/headphones/pr?sid=0pm%2Cfcn&otracker=categorytree&p%5B%5D=facets.connectivity%255B%255D%3DBluetooth&fm=neo%2Fmerchandising&iid=M_df83bcfd-f03d-4cc6-9002-eb15a09ec60b_1_372UD5BXDFYS_MC.R08R6GB1Q1BI&otracker=hp_rich_navigation_2_1.navigationCard.RICH_NAVIGATION_Electronics~Audio~Bluetooth%2BHeadphones_R08R6GB1Q1BI&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_2_L2_view-all&cid=R08R6GB1Q1BI']

    # rules = (
    #     # Extract links matching 'category.php' (but not matching 'subsection.php')
    #     # and follow links from them (since no callback means follow=True by default).
    #     #Rule(LinkExtractor(allow=(r"category\.php",), deny=(r"subsection\.php",))),
    #     # Extract links matching 'item.php' and parse them with the spider's method parse_item
    #     Rule(LinkExtractor(restrict_xpaths=('//a[@class="_2rpwqI"]')),callback="parse_product"),
    # )
    allowed_domains = ["example.com"]
    start_urls = ["http://www.example.com"]

    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(LinkExtractor(allow=(r"category\.php",), deny=(r"subsection\.php",))),
        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        Rule(LinkExtractor(allow=(r"item\.php",)), callback="parse_product"),
    )

    #rules = (Rule(LinkExtractor(allow=(r'.html')), callback="parse_product"))
    # sitemap_urls = ['https://www.target.com/sitemap_pdp-index.xml.gz']
    # sitemap_rules = [('/p/', "parse_product")]
    # sitemap_follow = ['/pdp/']

    def parse_product(self, response):
        # Using item loaders 
        # l = ItemLoader(item=ProductItem(),response=response)
        # l.add_xpath('name', '//h1[@id="pdp-product-title-id"]')
        # l.add_xpath('description', '//*[@id="specAndDescript"]/div[1]/div[2]/div[1]')
        # l.add_xpath('upc', '//div[@data-test="item-details-specifications"]/div/b[contains(text(),"UPC")]/parent::div')
        # l.add_value('product_url', response.url)
        # l.add_xpath('image_url', '//*[@id="pageBodyContainer"]/div/div[1]/div[2]/div[1]/div/section/div[2]/div[1]/div/button[1]/div/div/div/div/img/@src')
        # return l.load_item()
        yield {
            "url":response.url
        }