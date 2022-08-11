import scrapy
from CBR.items import CbrItem

# Typing
from typing import Generator
from scrapy.http.response.html import HtmlResponse

class CbrTableReservesSpider(scrapy.Spider):
    name = 'cbr_table_reserves'

    def __init__(self, data_from:str="01.1993", data_to:str="08.2022") -> None:
        super(CbrTableReservesSpider, self).__init__()
        self.start_urls = 'https://cbr.ru/hd_base/mrrf/mrrf_m/'
        self.data_from = data_from
        self.data_to = data_to
       

    def start_requests(self) -> Generator[scrapy.FormRequest, None, None]:
        yield scrapy.FormRequest(
            url=self.start_urls,
            method='GET',
            formdata={
                'UniDbQuery.Posted': "True",
                'UniDbQuery.From': self.data_from,
                'UniDbQuery.To': self.data_to})



    def parse(self, response:HtmlResponse) -> Generator[scrapy.Item, None, None]:
        for tr in response.xpath('//table[@class="data spaced"]//tr')[3:]:
            items = CbrItem()

            items['data'] = tr.xpath('.//td//text()')[0].get()
            items['inter_reserves'] = tr.xpath('.//td//text()')[1].get()
            items['currency_reserves'] = tr.xpath('.//td//text()')[2].get()
            items['foreign_currency'] = tr.xpath('.//td//text()')[3].get()
            items['sdr_account'] = tr.xpath('.//td//text()')[4].get()
            items['position_imf'] = tr.xpath('.//td//text()')[5].get()
            items['monetary_gold'] = tr.xpath('.//td//text()')[6].get()

            yield items