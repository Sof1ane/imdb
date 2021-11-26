import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CrawlImdSpider(CrawlSpider):
    name = 'crawl_imdb_films'
    allowed_domains = ['www.imdb.com']
    start_urls = ['https://www.imdb.com/chart/top/?ref_=nv_mv_250']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//tbody/tr/td[@class='titleColumn']"), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        item['titre'] = response.xpath('//*[@class="TitleHeader__TitleText-sc-1wu6n3d-0 dxSWFG"]/text()').get()
        item['titre_original'] = response.xpath('//div[@data-testid="hero-title-block__original-title"]/text()').get()
        item['score'] = response.xpath('//span[@class="AggregateRatingButton__RatingScore-sc-1ll29m0-1 iTLWoV"]/text()').extract_first()
        item['genre'] = response.xpath("//div[@class='ipc-chip-list GenresAndPlot__GenresChipList-cum89p-4 gtBDBL']/a/span/text()").getall()
        item['date'] = response.xpath('//div[@data-testid="title-details-section"]/ul/li[1]/div/ul/li/a/text()').get()
        item['duree'] = response.xpath('//div[@class="TitleBlock__TitleMetaDataContainer-sc-1nlhx7j-2 hWHMKr"]/ul/li[3]/text()').getall()
        item['synopsis'] = response.xpath('//span[@data-testid="plot-xl"]/text()').get()
        item['public'] = response.xpath('//div[@class="TitleBlock__TitleMetaDataContainer-sc-1nlhx7j-2 hWHMKr"]/ul/li[2]/span/text()').get()
        item['acteurs'] = response.xpath("//a[@data-testid='title-cast-item__actor']/text()").getall()
        item['langue_originale'] = response.xpath("//li[@data-testid='title-details-languages']/div/ul/li/a/text()").get()
        item['pays_original'] = response.xpath("//li[@data-testid='title-details-origin']/div/ul/li/a/text()").get()
        return item

