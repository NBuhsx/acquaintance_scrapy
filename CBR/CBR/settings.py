from pathlib import Path
from datetime import datetime

BOT_NAME = 'CBR'

SPIDER_MODULES = ['CBR.spiders']
NEWSPIDER_MODULE = 'CBR.spiders'

ROBOTSTXT_OBEY = True

FEEDS={
    Path('result', f'cdr_{datetime.now().strftime("%d-%m-%Y_%H-%M")}.json'): {
        'format': 'json',
        'encoding': 'utf8',
        'store_empty': False,
        'fields': None,
        'indent': 4,
        'item_export_kwargs': {
           'export_empty_fields': True,
        },
    },
    Path('result', f'cdr_{datetime.now().strftime("%d-%m-%Y_%H-%M")}.csv'): {
        'format': 'csv',
        'gzip_compresslevel': 5,
        'encoding': 'utf8'
    },
}

