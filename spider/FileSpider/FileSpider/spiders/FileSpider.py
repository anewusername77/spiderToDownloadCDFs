import scrapy
from FileSpider.items import FilespiderItem

class FilespiderSpider(scrapy.Spider):
    name = 'FileSpider'
    allowed_domains = ['spdf.gsfc.nasa.gov']
    start_urls = ['https://spdf.gsfc.nasa.gov/pub/data/polar/uvi/uvi_level1/1996/']

    def parse(self, response):
        item = FilespiderItem()  # 实例化item
        url = 'https://spdf.gsfc.nasa.gov/pub/data/polar/uvi/uvi_level1/1996/'
        #item['furls'] = response.css("td.line-content span.html-tag a::attr(href)").extract()[0] # 注意这里是一个集合也就是多张图片
        item['furls'] = response.xpath("//@href").extract()
        item['furls'] = item['furls'][5:]
        for i in range(0, len(item['furls'])):
            item['furls'][i] = url + item['furls'][i]

        yield item
        pass

