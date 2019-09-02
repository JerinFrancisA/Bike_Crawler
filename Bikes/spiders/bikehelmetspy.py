# -*- coding: utf-8 -*-
import scrapy
from ..items import BikesItem


class BikespySpider(scrapy.Spider):
    name = 'bikehelmetspy'
    start_urls = [
        'https://www.amazon.in/s?i=automotive&bbn=5258392031&rh=n%3A4772060031%2Cn%3A%214772061031%2Cn%3A5257478031%2Cn%3A5258045031%2Cn%3A5258392031%2Cp_85%3A10440599031&pf_rd_i=5258045031&pf_rd_m=A1K21FY43GMZF8&pf_rd_p=0da2298e-ae9e-4b16-8e83-6a3410e62dfd&pf_rd_r=SPESDE2T7MZ4VMQYAPGN&pf_rd_s=merchandised-search-3&pf_rd_t=101&ref=s9_acss_bw_cg_Heltype_3d1_w',
        'https://www.amazon.in/s?i=automotive&bbn=5258392031&rh=n%3A4772060031%2Cn%3A4772061031%2Cn%3A5257478031%2Cn%3A5258045031%2Cn%3A5258392031%2Cp_85%3A10440599031&page=2&pf_rd_i=5258045031&pf_rd_m=A1K21FY43GMZF8&pf_rd_p=0da2298e-ae9e-4b16-8e83-6a3410e62dfd&pf_rd_r=SPESDE2T7MZ4VMQYAPGN&pf_rd_s=merchandised-search-3&pf_rd_t=101&qid=1567426649&ref=sr_pg_2',
        'https://www.amazon.in/s?i=automotive&bbn=5258390031&rh=n%3A4772060031%2Cn%3A%214772061031%2Cn%3A5257478031%2Cn%3A5258045031%2Cn%3A5258390031%2Cp_85%3A10440599031&pf_rd_i=5258045031&pf_rd_m=A1K21FY43GMZF8&pf_rd_p=0da2298e-ae9e-4b16-8e83-6a3410e62dfd&pf_rd_r=FAEFY617NZX98JQB1XA5&pf_rd_s=merchandised-search-3&pf_rd_t=101&ref=s9_acss_bw_cg_Heltype_3a1_w',
        '',
    ]

    def parse(self, response):
        items = BikesItem()
        all_items = response.css('.s-include-content-margin')
        for item in all_items:
            item_name = item.css('.a-color-base.a-text-normal').css('::text').extract_first()
            item_url = item.css('.s-image-square-aspect .s-image').css('::attr(src)').extract_first()
            item_price = item.css('.a-price-whole').css('::text').extract_first()

            items['item_name'] = item_name
            items['item_url'] = item_url
            items['item_price'] = item_price

            yield items

