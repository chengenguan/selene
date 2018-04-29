#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2018-04-28
# @Author   : Chengen Guan: github: chengenguan (2630109260@qq.com)
# @Link     : https://github.com/chengenguan/selene
# @Version  : 0.1

import re
grp_re = re.compile('(\w+?).*(\d+?)')
print('match: ', grp_re.match('abc123').groups(), grp_re.match('abc123').start(), \
      grp_re.match('abc123').end(), grp_re.match('abc123').span())
find_re = re.compile('\d+')
print('findall: ', find_re.findall('12 adb, 34 cde, dd 66'))
intelcpu = re.compile('i\d?-\d{1,4}\w?')
print('findall: ', intelcpu.findall('i5-2345u   i7-123p  i3-6734'))
color = re.compile(r'red|yellow|blue')
msg = 'red hat yellow banana blue gogo'
print('sub: ', re.sub(pattern = color, repl = 'color', string = msg))
print('sub: ', re.sub(r'0x(\d+)', '123', 'number is 0x12347545454343'))
print('sub: ', re.sub(r'0x\d+', '123', 'number is 0x12347545454343'))
print('sub: ', color.sub(repl = 'color', string = msg))
print('subn: ', color.subn(repl = 'color', string = msg))
print('findall: ', re.findall(r'0x(\d+)', 'number is 0x12347545454343aa0x345'))
print('findall: ', re.findall(r'0x\d+', 'number is 0x12347545454343'))
print('findall: ', re.findall(r'0x(\d+)-(\d+)', 'number is 0x12347545454343-2345'))
print('split: ', re.split(r'0x(\d+)', 'number is 0x12347545454343'))
print('split: ', re.split(r'0x\d+', 'number is 0x12347545454343  fff'))
s1 = 'this is a test for r \\n.'
print('findall: ', re.findall('\\\\n', s1), re.findall(r'\\n', s1))

