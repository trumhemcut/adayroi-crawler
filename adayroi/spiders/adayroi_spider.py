import scrapy

class AdayroiSpider(scrapy.Spider):
    name = "adayroi"

    start_urls = [
            "https://www.adayroi.com/thoi-trang-nu-m2"
    ]

    def parse(self, response):
        for product in response.css('div.item-content'):
            nextPage = product.css('div.title-info h4.post-title a::attr(href)').extract_first()
            if nextPage is not None:
                nextPage = response.urljoin(nextPage)
                yield scrapy.Request(nextPage, callback=self.parseDetail)
        
        nextPage = response.css('div.adr.pagination.compact a.next.item::attr(href)').extract_first()
        print 'Next Page: %s' % nextPage
        if nextPage is not None: 
            nextPage = response.urljoin(nextPage)
            yield scrapy.Request(nextPage, callback=self.parse)

    def parseDetail(self, response):
        imageUrls = response.css('#product_gallery div.thumbnails div.items div.item::attr(data-zoom-image)')
        imageUrlString = []

        for imageUrl in imageUrls:
            imageUrlString.append(imageUrl.extract())
        
        imageUrlString = ','.join(imageUrlString)

        yield {
            'productName': response.css('div.item-info-block h1.item-title::text').extract_first(),
            'shortDescription': response.xpath('//div[@id="product_excerpt"]/*').extract_first(),
            'price': response.css('#item_prices div.item-price::text').extract_first(),
            'category': response.css('#header__breadcrumb span.active.item.last-child span::text').extract_first(),
            'images': imageUrlString,
            'url': response.url
        }