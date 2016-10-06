import scrapy

class AdayroiSpider(scrapy.Spider):
    name = "adayroi"

    start_urls = [
            "https://www.adayroi.com/thoi-trang-nu-m2",
            "https://www.adayroi.com/thoi-trang-nam-m81"
    ]


    def parse(self, response):
        for product in response.css('div.item-content'):
           yield {
               'productName': product.css('div.title-info h4.post-title a::text').extract_first(),
               'price': product.css('div.title-info div.item-price span.amount-1 ::text').extract_first(),
               'productUrl': product.css('div.title-info h4.post-title a::attr(href)').extract_first(),
               'category': response.css('h1.cat-title ::text').extract_first()
           }
        
        nextPage = response.css('div.adr.pagination.compact a.next.item::attr(href)').extract_first()
        print 'Next Page: %s' % nextPage
        if nextPage is not None: 
            nextPage = response.urljoin(nextPage)
            yield scrapy.Request(nextPage, callback=self.parse)
