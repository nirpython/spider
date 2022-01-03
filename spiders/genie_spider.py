import scrapy

class nescapy(scrapy.Spider):
    name = 'genie'
    start_urls = ['https://www.facebook.com/kaushik.dhulipala.5']

    def parse(self,response):
        all_div = response.text
        yield {"title": all_div}