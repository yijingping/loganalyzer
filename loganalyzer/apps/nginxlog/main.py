from __future__ import unicode_literals
__author__ = "yijingping"
__email__ = "yijingping@99fang.com"
__license__ = "BSD License"

import re
import urlparse
from datetime import datetime, timedelta

def process_log(log_file_path):
    fo = open(log_file_path, 'rU')
    try:
        for line in fo:
            process_line(line)
    finally:
        fo.close()
        
def process_line(line):
    global data, lines, matched, last_hour
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
        url = process_url(match.group(4))
        cost_time = float(match.group(3))
        dd = data[url] = data.get(url, {})
        dd['count'] = dd.get('count', 0) + 1
        dd['total_time'] = dd.get('total_time', 0.0) + cost_time
        dd['avg_time'] = dd['total_time'] / dd['count']

def process_data()
    global data, matched, lines, last_hour
    # echo data
    import pprint
    pprint.pprint(data)
    pprint.pprint("matched / lines = %s / %s"%(matched, lines))

def process_url(url):
    ''' 去掉url中的get参数和尾部的数字'''
    res = urlparse.urlparse(url).path
    pat = (r'(.+/)\d+/$')
    match = re.search(pat, res)
    if match:
        res = match.group(1)

    return res


if __name__ == '__main__':
    global data, matched, lines, last_hour
    data = {}
    lines = 0
    matched = 0
    last_hour = datetime.now() - timedelta(hours=1)

    # set nginx access log file path, standard format
    log_file_path = 'mapi_uwsgi_access.log'
    # process log 
    process_log(log_file_path)
    # process data
    process_data()

