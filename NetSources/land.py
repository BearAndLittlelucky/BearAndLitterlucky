#!/usr/bin/env python
# _*_encoding: utf-8_*_
'''
@author: 小熊与小幸的故事
@license: (C) Copyright 2020-, Node Supply Chain Manager Corporation Limited.
@file: land.py
@time: 2020/9/8 19:55
@desc:
'''
import IMS.NetSources.file_operation as files
import json

def examine_name_pwd():
    #验证账号密码是否正确
    user_name = input('输入账号：')
    user_psw = input('请输入密码：')
    file = '..\\UserInfo\\'+user_name+'.json'
    dict1 = {}
    try:
        dict1 = json.loads(files.basic_file_read(file)) #通过loads将json格式的文件转换成python格式的字典
    except:
         print('该账号未注册')
         return
    if dict1[user_name] == user_psw:
             print('密码输入正确')
    else:
        print('密码输入错误')
        return
    return file

def landing_menu(file):
    #学生信息关系系统主界面
    while True:
        print('''
            1.查看学生信息
            2.添加学生信息
            3.修改学生信息
            4.删除学生信息
            5.退出
        ''')

        order = input('请输入-->')
        if order == '1':
            ##查看学生信心
            showall(file)
        elif order == '2':
            #添加学生信息
            addstu(file)
        elif order == '3':
            #修改学生信息
            exchange(file)
        elif order == '4':
            #删除学生信息
            delstu(file)
        else:
            #退出
            break

def showall(file):
    #展示所有学生信息的函数
    all_content = json.loads(files.basic_file_read(file))
    for key in all_content['student'].keys():
        print('姓名：%s,年龄：%s，性别：%s'%(key,all_content['student'][key]['age'],all_content['student'][key]['sex']))


def addstu(file):
    #添加学生信息的函数
    new_stu_name = input('请输入学生姓名:')
    new_stu_age = input('请输入学生年龄:')
    new_stu_sex = input('请输入学生性别:')
    with open(file,'r',encoding='utf-8') as addstus:
        content = json.load(addstus)
        content['student'][new_stu_name]={'age':new_stu_age,'sex':new_stu_sex}
    with open(file,'w',encoding='utf-8') as f:
        json.dump(content,f)
    print('添加成功')

def exchange(file):
    #修改学生信息的函数 先不考虑重名的情况
    find_name = input('请输入要修改的学生姓名：')
    with open(file,'r',encoding='utf-8') as allstus:
        content =json.load(allstus)
        for key  in content['student'].keys():
            if key == find_name :
                #如果找到这位同学
                finde_key=input('请输入要修改的类型(age,sex)：')
                finde_content = input('请输入修改的内容：')
                content['student'][key][finde_key] = finde_content
                print('修改成功')
                break
        else:
            print('未找到这名同学的信息')
    with open(file,'w',encoding='utf-8') as allstus:
        json.dump(content,allstus)

def delstu(file):
    #删除学生信息的模块
    delstu_name = input('请输入要删除的学生的姓名：')
    with open(file,'r',encoding='utf-8') as allstus:
        content =json.load(allstus)
        for key  in content['student'].keys():
            if key == delstu_name :
                del content['student'][key]
                print('删除成功')
                break
        else:
            print('未找到这名同学的信息')
    with open(file,'w',encoding='utf-8') as allstus:
        json.dump(content,allstus)
def landing():
    #登录后先执行账号密码验证函数 在执行主函数
    file = examine_name_pwd()
    landing_menu(file)