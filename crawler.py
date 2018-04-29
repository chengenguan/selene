#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2018-04-28
# @Author   : Chengen Guan: github: chengenguan (2630109260@qq.com)
# @Link     : https://github.com/chengenguan/selene
# @Version  : 0.1

# Get picture from Douban shy group
# <td class="title">
#     <a href="https://www.douban.com/group/topic/116329734/" title="【晒】这么粗的腿发朋友圈竟然没人说粗。。。" class="">
#          晒】这么粗的腿发朋友圈竟然没人说粗。。。
#     </a>
# </td>
#     
# <img src="https://img3.doubanio.com/view/group_topic/large/public/p115195406.jpg" width="500">
# <img src="https://img3.doubanio.com/view/group_topic/large/public/p115195395.jpg" width="500">
     

from urllib import request
from urllib import parse
from urllib import error
import re
import os
import time
import chardet

def getHtml(url, headers=None):
    req = request.Request(url, headers=headers)
    try:
        with request.urlopen(req, timeout=10) as f:
            data = f.read()
            #encode_type = chardet.detect(data)['encoding'] if chardet.detect(data)['confidence'] > 0.9 else 'utf-8'
            #return data.decode(encode_type)
            return data
    except:
        print('Content Error from URL %s' % url)

def getJPG(data):
    for line in data:
        print(line)

if __name__ == '__main__':
    topicReg = re.compile(r'<a href="(https://www.douban.com/group/topic/.*?)"')
    jpgReg = re.compile(r'<img src="(https://img[1-9].doubanio.com/.*?large.*?jpg)"')
    # groupURL = 'https://www.douban.com/group/haixiuzu/'
    
    # https://www.douban.com/group/haixiuzu/discussion?start=50 75 100
    baseURL = 'https://www.douban.com/group/haixiuzu/discussion?start='
    step = 25
    for i in range(5):
        groupURL = baseURL + str(step*i)
        user_agent = 'Mozilla/5.0 (X11; Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.84 Safari/537.36'
        headers = {'User-Agent': user_agent}

        groupHtml = getHtml(groupURL, headers)
        topicURL = re.findall(topicReg, groupHtml.decode('utf-8'))
        #topicURL = re.findall(topicReg, groupHtml)
        print(topicURL)
        for each_topic in topicURL:
            time.sleep(0.5)
            topicHtml = getHtml(each_topic, headers)
            jpgURL = re.findall(jpgReg, topicHtml.decode('utf-8'))
            print(jpgURL)
            for g in jpgURL:
                with open('/home/pi/Pictures/' + g.split('/')[-1], 'wb') as f:
                    f.write(request.urlopen(g).read())

                

        


    



    
