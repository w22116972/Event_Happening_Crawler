from scrapy.exceptions import DropItem
from scrapy import signals
import re

class EventPipeline(object):
    def process_item(self, item, spider):
        if len(item['address']) == 0:
            raise DropItem("NO Address !")
        elif len(item['title']) == 0:
            raise DropItem("No Title !")
        else:
            item['address'] = re.search(u'[台臺]北市.*號', item['address'][0])[0]
            return item

'''
台北市 / 台北市大安區信義路三段147巷11弄6-1號(捷運大安站1號
台北市復興北路1號3樓之1 / 亞細亞通商大樓 (忠孝復興5號出口) / 台北市復興北路1號
台北市衡陽路51號6樓之2 / 台北市衡陽路51號
台北市大安區 / 台北市大安區信義路三段147巷11弄6-1號 (近捷運大安站,信義線1號
台北市復興北路48號 11F-3 (GliaCloud辦公室) 
台北市大安區忠孝東路四段169號4F之1 /  台北市大安區忠孝東路四段169號
台北市（地點另通知） / 台北市中正區中山北路一段2號
台北市復興北路1號3樓之1 / 亞細亞通商大樓 (忠孝復興5號出口) / 台北市復興北路1號

台北市中山區長安東路一段61-1號
'''
