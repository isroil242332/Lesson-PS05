import scrapy
urls = 'https://www.divan.ru/category/svet'

class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        lightings = response.css("div._Ud0k")
        for light in lightings:
            yield {
                "name" : light.css("div.lsooF span::text").get(),
                "price" : light.css("div.q5Uds span::text").get(),
                "url" : urls + light.css("a").attrib["href"]
            }
