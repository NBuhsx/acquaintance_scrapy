import scrapy

# Typing
from typing import Dict, Generator, List
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


# Scrapy не может вернуть список (так как возращает: Словарь, Запрос, Items), я намеренно не стал использовать Items, поэтому пришлось сделать небольшой обход
    def parse(self, response:HtmlResponse) -> Generator[Dict[int, List[str]], None, None]:
        for tr in response.xpath('//table[@class="data spaced"]//tr')[3:]:
            yield {1:[tb.get() for tb in tr.xpath('.//td//text()')]}
            