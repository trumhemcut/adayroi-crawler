import scrapy


class AdayroiSpider(scrapy.Spider):
    name = "adayroi"

    start_urls = [
        'https://www.adayroi.com/thuc-uong-m713?p=1',
        'https://www.adayroi.com/thuc-uong-m713?p=2',
        'https://www.adayroi.com/thuc-uong-m713?p=3',
        'https://www.adayroi.com/thuc-uong-m713?p=4',
        'https://www.adayroi.com/thuc-uong-m713?p=5',
        'https://www.adayroi.com/thuc-uong-m713?p=6',
        'https://www.adayroi.com/thuc-uong-m713?p=7',
        'https://www.adayroi.com/thuc-uong-m713?p=8',
        'https://www.adayroi.com/thuc-uong-m713?p=9',
        'https://www.adayroi.com/thuc-uong-m713?p=10',
        'https://www.adayroi.com/thuc-uong-m713?p=11',
        'https://www.adayroi.com/thuc-uong-m713?p=12',
        'https://www.adayroi.com/thuc-uong-m713?p=13',
        'https://www.adayroi.com/thuc-uong-m713?p=14',
        'https://www.adayroi.com/thuc-uong-m713?p=15',
        'https://www.adayroi.com/thuc-uong-m713?p=16',
        'https://www.adayroi.com/thuc-uong-m713?p=17',
        'https://www.adayroi.com/thuc-uong-m713?p=18',
        'https://www.adayroi.com/thuc-uong-m713?p=19',
    ]


    def parse(self, response):
        for product in response.css('div.item-content'):
            yield {
                'productName': product.css('div.title-info h4.post-title a::text').extract_first(),
                'price': product.css('div.title-info div.item-price span.amount-1 ::text').extract_first(),
                'productUrl': product.css('div.title-info h4.post-title a::attr(href)').extract_first(),
                'category': response.css('h1.cat-title ::text').extract_first()
            }