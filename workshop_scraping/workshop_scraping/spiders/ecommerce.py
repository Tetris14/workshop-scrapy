import scrapy

class EcommerceSpider(scrapy.Spider):
    name = 'ecommerce'
    allowed_domains = ['webscraper.io']
    start_urls = ['https://webscraper.io/test-sites/e-commerce/static']

    def parse(self, response):
        products = response.xpath('/html/body/div[1]/div[3]/div/div[2]/div[2]')
        if not products:
            raise scrapy.exceptions.CloseSpider('No products found')
        print('Products found:', len(products))
        pass