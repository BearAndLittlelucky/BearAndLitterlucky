#!/usr/bin/env python
# _*_encoding: utf-8_*_
'''
@author: 小熊与小幸的故事
@license: (C) Copyright 2020-, Node Supply Chain Manager Corporation Limited.
@file: file_operation.py
@time: 2020/9/8 19:54
@desc:
'''
import json

def basic_file_read(file):
    #普通文本文件的读取
    with open(file,'r',encoding='utf-8') as f:
        return f.read()

def basic_file_write(file,content):
    #普通文本文件的写
    content = json.dumps(content)
    with open(file,'w',encoding='utf-8') as f:
        f.write(content)