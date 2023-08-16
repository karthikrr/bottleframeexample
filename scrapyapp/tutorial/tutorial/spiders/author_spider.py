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

This module uses response.follow_all method to generate the request object
'''

class AuthorSpider(scrapy.Spider):
    name="author"

    def start_requests(self):
        urls = ["https://quotes.toscrape.com/"]
        for url in urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        author_page_links = response.css(".author + a")
        yield from response.follow_all(author_page_links, self.parse_author)

        pagination_links = response.css("li.next a")
        yield from response.follow_all(pagination_links, self.parse)

    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).get(default="").strip()

        yield {
            "name": extract_with_css("h3.author-title::text"),
            "birthdate": extract_with_css(".author-born-date::text"),
            "bio": extract_with_css(".author-description::text"),
        }