from pathlib import Path

import scrapy

'''
To create scrapy project run below command
scrapy startproject tutorial

Then create spiders inside spider folder with unique name provided in the class name

Then run the spider using below command
scrapy crawl quotes

To save the scraped data to json file using -O output.json  -O= override

scrapy crawl extract -O output.json

To save the scraped data to jsonline file using -o append mode
scrapy crawl extract -o output.jsonl

'''

class ExtractSpider(scrapy.Spider):
    name="extract"

    def start_requests(self):
        urls = ["https://quotes.toscrape.com/page/1/",
            "https://quotes.toscrape.com/page/2/",]
        for url in urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get(),
                "tags": quote.css("div.tags a.tag::text").getall(),
            }