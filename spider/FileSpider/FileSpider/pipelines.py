# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.files import FilesPipeline
from scrapy import Request
import os
class FilespiderPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        # 循环每一张图片地址下载，若传过来的不是集合则无需循环直接yield
        for f_url in item['furls']:
            yield Request(f_url)

    def file_path(self, request, response=None, info=None):

        path = os.path.join('E:\\aurora\\spider\\download', request.url.split("/")[-1])
        return path
