from itemadapter import ItemAdapter
from scrapy.exporters import CsvItemExporter


class CsvExportPipeline:
    """Simple csv export"""

    def open_spider(self, spider):
        self.year_to_exporter = {}

    def close_spider(self, spider):
        for exporter, csv_file in self.year_to_exporter.values():
            exporter.finish_exporting()
            csv_file.close()

    def _exporter_for_item(self, item):     
        csv_file = open(f"target.csv", "wb+")
        exporter = CsvItemExporter(csv_file, include_headers_line=True, join_multivalued=',')
        exporter.start_exporting()
        self.year_to_exporter = (exporter, csv_file)
        return self.year_to_exporter

    def process_item(self, item, spider):
        exporter = self._exporter_for_item(item)
        exporter.export_item(item)
        return item