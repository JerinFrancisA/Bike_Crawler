# -*- coding: utf-8 -*-
import scrapy
from ..items import BikesItem


class BikeallspySpider(scrapy.Spider):
    name = 'bikeallspy'
    start_urls = [
        'https://www.amazon.in/s?i=automotive&bbn=5258392031&rh=n%3A4772060031%2Cn%3A%214772061031%2Cn%3A5257478031%2Cn%3A5258045031%2Cn%3A5258392031%2Cp_85%3A10440599031&pf_rd_i=5258045031&pf_rd_m=A1K21FY43GMZF8&pf_rd_p=0da2298e-ae9e-4b16-8e83-6a3410e62dfd&pf_rd_r=SPESDE2T7MZ4VMQYAPGN&pf_rd_s=merchandised-search-3&pf_rd_t=101&ref=s9_acss_bw_cg_Heltype_3d1_w',
        'https://www.amazon.in/s?i=automotive&bbn=5258390031&rh=n%3A4772060031%2Cn%3A%214772061031%2Cn%3A5257478031%2Cn%3A5258045031%2Cn%3A5258390031%2Cp_85%3A10440599031&pf_rd_i=5258045031&pf_rd_m=A1K21FY43GMZF8&pf_rd_p=0da2298e-ae9e-4b16-8e83-6a3410e62dfd&pf_rd_r=FAEFY617NZX98JQB1XA5&pf_rd_s=merchandised-search-3&pf_rd_t=101&ref=s9_acss_bw_cg_Heltype_3a1_w',
        'https://www.amazon.in/s?i=automotive&bbn=5258042031&rh=n%3A4772060031%2Cn%3A%214772061031%2Cn%3A5257478031%2Cn%3A5257575031%2Cn%3A5258042031%2Cp_85%3A10440599031&pf_rd_i=5257478031&pf_rd_m=A1K21FY43GMZF8&pf_rd_p=bd3ba4d6-2c95-4851-9fe1-3d1d7cf71d74&pf_rd_r=75DJC694E9VZZMKAZDAN&pf_rd_s=merchandised-search-8&pf_rd_t=101&ref=s9_acss_bw_cg_BKSafety_4a1_w',
        'https://www.amazon.in/s?i=automotive&bbn=5258050031&rh=n%3A4772060031%2Cn%3A%214772061031%2Cn%3A5257478031%2Cn%3A5257575031%2Cn%3A5258050031%2Cp_85%3A10440599031&s=price-desc-rank&pf_rd_i=5257478031&pf_rd_m=A1K21FY43GMZF8&pf_rd_p=bd3ba4d6-2c95-4851-9fe1-3d1d7cf71d74&pf_rd_r=GWY7511V5XQF6H84MHG8&pf_rd_s=merchandised-search-8&pf_rd_t=101&ref=s9_acss_bw_cg_BKSafety_4b1_w',
        'https://www.amazon.in/s?k=biker+face+mask&i=automotive&rh=n%3A4772060031%2Cp_6%3AAT95IG9ONZD7S%2Cp_85%3A10440599031&pf_rd_i=5257478031&pf_rd_m=A1K21FY43GMZF8&pf_rd_p=bd3ba4d6-2c95-4851-9fe1-3d1d7cf71d74&pf_rd_r=E9EX8YR968BFB2SX6Y8J&pf_rd_s=merchandised-search-8&pf_rd_t=101&ref=s9_acss_bw_cg_BKSafety_4c1_w',
        'https://www.amazon.in/s?k=crash+guard+for+bike&rh=p_85%3A10440599031&pf_rd_i=5257478031&pf_rd_m=A1K21FY43GMZF8&pf_rd_p=bd3ba4d6-2c95-4851-9fe1-3d1d7cf71d74&pf_rd_r=FKRZGAMK7SZRP0X117K1&pf_rd_s=merchandised-search-8&pf_rd_t=101&ref=s9_acss_bw_cg_BKSafety_5a1_w',
        'https://www.amazon.in/s?k=engine+oil+for+bike&pf_rd_i=5257478031&pf_rd_m=A1K21FY43GMZF8&pf_rd_p=eca27583-bc82-4947-9754-656d407adfd0&pf_rd_r=XTNQTEXNTY139QMM8RH5&pf_rd_s=merchandised-search-10&pf_rd_t=101&ref=s9_acss_bw_cg_BKPR_3a1_w',
        'https://www.amazon.in/s?i=automotive&bbn=5257570031&rh=n%3A4772060031%2Cn%3A%214772061031%2Cn%3A5257478031%2Cn%3A5257570031%2Cp_85%3A10440599031&pf_rd_i=5257478031&pf_rd_m=A1K21FY43GMZF8&pf_rd_p=eca27583-bc82-4947-9754-656d407adfd0&pf_rd_r=SW51S5AKQEN25HA18K3S&pf_rd_s=merchandised-search-10&pf_rd_t=101&ref=s9_acss_bw_cg_BKPR_3b1_w',
        'https://www.amazon.in/s?k=rims+and+alloy+wheels+for+bike&i=automotive&rh=n%3A4772060031%2Cn%3A5257478031%2Cn%3A5257578031%2Cp_85%3A10440599031&pf_rd_i=5257478031&pf_rd_m=A1K21FY43GMZF8&pf_rd_p=eca27583-bc82-4947-9754-656d407adfd0&pf_rd_r=K232EBDMKR425YX4SGX6&pf_rd_s=merchandised-search-10&pf_rd_t=101&ref=s9_acss_bw_cg_BKPR_4d1_w',
        'https://www.amazon.in/s?i=automotive&bbn=5257919031&rh=n%3A4772060031%2Cn%3A%214772061031%2Cn%3A5257478031%2Cn%3A5257561031%2Cn%3A5257919031%2Cp_85%3A10440599031&pf_rd_i=5257478031&pf_rd_m=A1K21FY43GMZF8&pf_rd_p=0588bcc2-91b8-4087-82a1-8c04de919b60&pf_rd_r=6A3CA12X74KA5W4RA41G&pf_rd_s=merchandised-search-12&pf_rd_t=101&ref=s9_acss_bw_cg_BKAcc_3a1_w',
        'https://www.amazon.in/s?k=mobile+holder+for+bike+%7C+mobile+bike+charger&i=automotive&bbn=4772060031&rh=n%3A4772060031%2Cp_6%3AAT95IG9ONZD7S&pf_rd_i=5257478031&pf_rd_m=A1K21FY43GMZF8&pf_rd_p=0588bcc2-91b8-4087-82a1-8c04de919b60&pf_rd_r=JBZ9ZAY4SK4W682YTAZW&pf_rd_s=merchandised-search-12&pf_rd_t=101&ref=s9_acss_bw_cg_BKAcc_3b1_w',
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
