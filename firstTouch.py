#!/usr/bin/python3
# -*- coding: utf-8 -*-
from urllib import request
from urllib import parse
from urllib import error
import json
import chardet


def getContent(url, data=None, headers=None):
    req = request.Request(url, data, headers)
    try:
        with request.urlopen(req, timeout=10) as f:
            data = f.read()
            print('headers:', json.dumps(f.getheaders()))
            print('Original URL:', url)
            print('Redirected URL:', f.geturl())
            print('Info: ', f.info())
            print('Info class: ', f.info().__class__)
            encode_type = chardet.detect(data)['encoding'] if chardet.detect(data)['confidence'] > 0.9 else 'utf-8'
            print('encoding type: ', encode_type)
            return data.decode(encode_type)
    except error.URLError as e:
        if hasattr(e, 'reason'):
            print('Reason:',e.reason)
        elif hasattr(e, 'code'):
            print('Error code:', e.code)

if __name__ == '__main__':
    # url = 'http://www.douban.com/'
    # url = 'file:///home/pi/guan/selene/testdata.txt'
    # url = 'http://127.0.0.1:8888'   # nc -l 8888
    url = 'http://weibo.com/u/auxten'
    values = [ ('name', 'guan'), ('age', 40) ]
    user_agent = 'Mozilla/5.0 (X11; Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.84 Safari/537.36'
    data = parse.urlencode(values).encode('utf-8')
    url = url + '?' + data.decode('utf-8')
    headers = {'User-Agent': user_agent}
    print('url: %s | post data: %s | headers: %s' % (url, data, headers))
    response = getContent(url = url, headers = headers)
    # response = getContent(url = url, data = data, headers = headers)
    print(response)
