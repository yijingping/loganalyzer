# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import urlparse
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand, CommandError
from loganalyzer.apps.nginxlog.models import Accesstime 

class Command(BaseCommand):
    args = 'log_file_path'
    help = '分析过去一个小时内url的访问次数和访问时间'

    data = {}
    lines = 0
    matched = 0
    last_hour = datetime.now() - timedelta(hours=1)

    def handle(self, *args, **options):
        log_file_path = args[0] 
        # process log 
        self.process_log(log_file_path)
        # process data
        self.process_data()

    def process_log(self, log_file_path):
        fo = open(log_file_path, 'rU')
        try:
            for line in fo:
                self.process_line(line)
        finally:
            fo.close()

    def process_line(self, line):
        data, lines, matched, last_hour = self.data, self.lines, self.matched, self.last_hour
        lines += 1
        pat = (r''
               '(\d+.\d+.\d+.\d+)\s-\s-\s' #IP address
               '\[%s(.+)\]\s' #datetime
               '(\d+.\d+)\s' #cost time
               '".+\s(.+)\s\w+/.+"\s\d+\s' #requested url
               '\d+\s"(.+)"\s' #referrer
               '"(.+)"' #user agent
               %(last_hour.strftime('%d/%b/%Y:%H'))
              )
        match = re.search(pat, line)
        if match:
            matched += 1
            url = self.process_url(match.group(4))
            cost_time = float(match.group(3))
            dd = data[url] = data.get(url, {})
            dd['total'] = dd.get('total', 0) + 1
            dd['total_time'] = dd.get('total_time', 0.0) + cost_time
            dd['avg_time'] = dd['total_time'] / dd['total']

    def process_data(self):
        data, lines, matched, last_hour = self.data, self.lines, self.matched, self.last_hour
        for k,v in data.iteritems():
            print k,v
            try:
                obj = Accesstime.objects.get(ip='127.0.0.1', host='yjp-pc', url=k, date=last_hour.date(), hour=last_hour.hour)
            except Accesstime.DoesNotExist:
                obj = Accesstime(ip='127.0.0.1', host='yjp-pc', url=k, date=last_hour.date(), hour=last_hour.hour)

            obj.total = v['total']
            obj.total_time = v['total_time']
            obj.avg_time = v['avg_time']
            obj.save()

        # echo data
        import pprint
        pprint.pprint(data)
        pprint.pprint("matched / lines = %s / %s"%(matched, lines))

    def process_url(self, url):
        ''' 去掉url中的get参数和尾部的数字'''
        res = urlparse.urlparse(url).path
        pat = (r'(.+/)\d+/$')
        match = re.search(pat, res)
        if match:
            res = match.group(1)

        return res
