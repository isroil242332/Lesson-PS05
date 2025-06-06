import scrapy
import csv
urls = 'https://www.divan.ru/category/svet'
parsed_data = []
class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        lightings = response.css("div._Ud0k")
        for light in lightings:

            pars3 = {
                "name" : light.css("div.lsooF span::text").get(),
                "price" : light.css("div.q5Uds span::text").get(),
                "url" : urls + light.css("a").attrib["href"]
            }


            yield pars3
            name3 = pars3.get("name")
            price3 = pars3.get("price")
            url3 = pars3.get("url")
            parsed_data.append([name3, price3, url3])

        with open("svet.csv", 'w',newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Название', 'Цена', 'Ссилка'])
            writer.writerows(parsed_data)