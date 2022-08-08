from scrapy.exporters import JsonItemExporter, CsvItemExporter

from pathlib import Path
from scrapy.utils.python import to_bytes
from typing import List, Dict

from CBR.items import ColumName


class MyJsonItemExporer(JsonItemExporter):
    def __init__(self, file:Path|str, **kwargs):
        super().__init__(file, **kwargs)

    def export_item(self, item:Dict[int, List[str]]):
        if self.first_item:
            self.first_item = False
        else:
            self.file.write(b',')
            self._beautify_newline()
        
        itemdict = dict(self._get_serialized_fields(ColumName.as_dict(*item[1])))
        data = self.encoder.encode(itemdict)
        self.file.write(to_bytes(data, self.encoding))


class MyCsvItemExporer(CsvItemExporter):
    def __init__(self, file, include_headers_line=True, join_multivalued=',', errors=None, **kwargs):
        super().__init__(file, include_headers_line, join_multivalued, errors, **kwargs)
        self.csv_writer.writerow(ColumName.as_tuple())

    
    def export_item(self, item:Dict[int, List[str]]):
        self.csv_writer.writerow(item[1])