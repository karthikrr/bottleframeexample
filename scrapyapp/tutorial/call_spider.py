# Call the spider using python script
from scrapy.crawler import CrawlerProcess
from tutorial.spiders.argument_spider import ArgumentSpider


crawler = CrawlerProcess()
crawler.crawl(ArgumentSpider, tag="humor")


