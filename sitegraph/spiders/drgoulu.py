# -*- coding: utf-8 -*-
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.utils.url import urljoin_rfc
from sitegraph.items import SitegraphItem


class DrGouluSpider(CrawlSpider):
    name = "drgoulu"
    allowed_domains = ["drgoulu.com"]
    start_urls = (
        'http://www.drgoulu.com/',
    )

    rules = (
        Rule(SgmlLinkExtractor(allow=r'/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        i = SitegraphItem()
        i['url'] = response.url
        # i['http_status'] = response.status
        llinks=[]
        for anchor in hxs.select('//a[@href]'):
            href=anchor.select('@href').extract()[0]
            if not href.lower().startswith("javascript"):
                llinks.append(urljoin_rfc(response.url,href))
        i['linkedurls'] = llinks
        return i