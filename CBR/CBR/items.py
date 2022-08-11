import scrapy
 
class CbrItem(scrapy.Item):
    data = scrapy.Field()               # Дата
    inter_reserves = scrapy.Field()     # Международные резервы
    currency_reserves = scrapy.Field()  # валютные резервы
    foreign_currency = scrapy.Field()   # иностранная валюта
    sdr_account = scrapy.Field()        # счет в СДР
    position_imf = scrapy.Field()       # резервная позиция в МВФ
    monetary_gold = scrapy.Field()      # монетарное золото
