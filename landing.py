#!/usr/bin/env python
# _*_encoding: utf-8_*_
'''
@author: 小熊与小幸的故事
@license: (C) Copyright 2020-, Node Supply Chain Manager Corporation Limited.
@file: landing.py
@time: 2020/9/13 18:39
@desc:
'''
from PyQt5.QtWidgets import QMessageBox

import IMS.FileOperation as files
import json

def examine_name_pwd(user_name,user_psw):
    print(user_name,user_psw)
    #验证账号密码是否正确
    # user_name = input('输入账号：')
    # user_psw = input('请输入密码：')
    file = 'D:\Project\IMS\\UserInfo\\' + user_name + '.json'
    dict1 = {}
    try:
        dict1 = json.loads(files.basic_file_read(file)) #通过loads将json格式的文件转换成python格式的字典
    except:
         QMessageBox.critical(self,'Warning', 'The account has been registered and please reregistered!!')

         return
    if dict1[user_name] == user_psw:
             print('密码输入正确')
    else:
        print('密码输入错误')
        return
    return file
