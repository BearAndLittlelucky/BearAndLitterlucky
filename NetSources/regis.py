#!/usr/bin/env python
# _*_encoding: utf-8_*_
'''
@author: 小熊与小幸的故事
@license: (C) Copyright 2020-, Node Supply Chain Manager Corporation Limited.
@file: regis.py
@time: 2020/9/8 19:55
@desc:
'''
#注册功能的实现
import IMS.NetSources.file_operation as files
#导入文件操作模块

def regist_menu():
    user_name = input('请输入用户名：')
    user_pwd = input('请输入密码：')
    user_repwd = input('请再次输入密码：')
    if user_pwd != user_repwd:
        #验证两次输入的密码是否相等
        print('输入的两次密码不相等，请重新注册')
        return
    file = '..\\UserInfo\\'+user_name+'.json' #将用户名设为json文件的文件名
    try:                                  #判断用户名是否存在
        with open(file,'r',encoding='utf-8'):
            print('该账号已被注册，请重新注册')
    except:
        content ={user_name:user_pwd,'student':{}} # 将用户名和密码以键值对的方式写入文件
        files.basic_file_write(file,content)  #调用文件写入函数
        print('注册成功')