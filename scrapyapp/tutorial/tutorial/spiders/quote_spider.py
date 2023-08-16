from pathlib import Path

import scrapy

'''
To create scrapy project run below command
scrapy startproject tutorial

Then create spiders inside spider folder with unique name provided in the class name

Then run the spider using below command
scrapy crawl quotes

'''

class QuoteSpider(scrapy.Spider):
    name="quotes"

    def start_requests(self):
        urls = ["https://quotes.toscrape.com/page/1/",
            "https://quotes.toscrape.com/page/2/",]
        for url in urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        page = response.url.split('/')[-2]
        filename = f'quotes-{page}.html'
        Path(filename).write_bytes(response.body)
        self.log(f'Saved file {filename}')