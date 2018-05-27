# -*- coding: utf-8 -*-

# Define your item pipelines here

#import json



#class JsonWriterPipeline(object):

 #   def __init__(self):
  #      self.file = open('items.jl', 'wb')

   # def process_item(self, item, spider):
    #    line = json.dumps(dict(item)) + "\n"
     #   self.file.write(line)
      #  return item
      
#from scrapy.exporters import XmlItemExporter

#class XmlItemExporter('io.BytesIO', item_element='item', root_element='items',):
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem

class MyImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item
     
class XmlItemExporter(object):
#class PerYearXmlExportPipeline(object):
   # """Distribute items across multiple XML files according to their 'year' field"""

    def open_spider(self, spider):
        self.year_to_exporter = {}

    def close_spider(self, spider):
        for exporter in self.year_to_exporter.values():
            exporter.finish_exporting()
            exporter.file.close()

    def _exporter_for_item(self, item):
        year = item['year']
        if year not in self.year_to_exporter:
            f = open('{}.xml'.format(year), 'wb')
            exporter = XmlItemExporter(f)
            exporter.start_exporting()
            self.year_to_exporter[year] = exporter
        return self.year_to_exporter[year]

    def process_item(self, item, spider):
        exporter = self._exporter_for_item(item)
        exporter.export_item(item)
        return item



class MyItem(scrapy.Item):

    # ... other item fields ...
    image_urls = scrapy.Field()
    images = scrapy.Field()


#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MytryPipeline(object):
    def process_item(self, item, spider):
        return item
