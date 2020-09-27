#!/usr/bin/env python
# _*_encoding: utf-8_*_
'''
@author: 小熊与小幸的故事
@license: (C) Copyright 2020-, Node Supply Chain Manager Corporation Limited.
@file: View.py
@time: 2020/9/21 22:15
@desc:
'''
import json
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import IMS.FileOperation as files




# def View(file):
#     print(file)
#     gridLayout = QtWidgets.QGridLayout()
#     gridLayout.setContentsMargins(0, 0, 0, 0)
#     gridLayout.setObjectName("gridLayout")
#     #输入栏
#     lineEdit = QtWidgets.QLineEdit()
#     sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
#     sizePolicy.setHorizontalStretch(5)
#     sizePolicy.setVerticalStretch(1)
#     sizePolicy.setHeightForWidth(lineEdit.sizePolicy().hasHeightForWidth())
#     lineEdit.setSizePolicy(sizePolicy)
#     lineEdit.setObjectName("lineEdit")
#     gridLayout.addWidget(lineEdit, 4, 1, 1, 2)
#     #查询按钮
#     pushButton = QtWidgets.QPushButton()
#     sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
#     sizePolicy.setHorizontalStretch(3)
#     sizePolicy.setVerticalStretch(1)
#     sizePolicy.setHeightForWidth(pushButton.sizePolicy().hasHeightForWidth())
#     pushButton.setSizePolicy(sizePolicy)
#     pushButton.setObjectName("pushButton")
#     pushButton.setText("查找")
#     gridLayout.addWidget(pushButton, 4, 4, 1, 1)
#     pushButton.clicked.connect(lambda :type(comboBox,lineEdit,file,model))
#     #选择查询方式
#     comboBox = QtWidgets.QComboBox()
#     sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
#     sizePolicy.setHorizontalStretch(3)
#     sizePolicy.setVerticalStretch(2)
#     sizePolicy.setHeightForWidth(comboBox.sizePolicy().hasHeightForWidth())
#     comboBox.setSizePolicy(sizePolicy)
#     comboBox.setObjectName("comboBox")
#     comboBox.addItem("查找全部")
#     comboBox.addItem("按学号查找")
#     comboBox.addItem("按姓名查找")
#     comboBox.addItem("按专业查找")
#     comboBox.addItem("按课程名查找")
#     gridLayout.addWidget(comboBox, 4, 3, 1, 1)
#     #显示模块
#     tableView = QtWidgets.QTableView()
#     sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
#     sizePolicy.setHorizontalStretch(0)
#     sizePolicy.setVerticalStretch(50)
#     sizePolicy.setHeightForWidth(tableView.sizePolicy().hasHeightForWidth())
#     tableView.setSizePolicy(sizePolicy)
#     tableView.setObjectName("tableView")
#     gridLayout.addWidget(tableView, 5, 1, 1, 4)
#
#     model = QStandardItemModel()
#     model.setHorizontalHeaderLabels(['Sno', 'Name', 'Age',"Sex","Is","Course"])
#     tableView.setModel(model)
#     # 水平方向标签拓展剩下的窗口部分，填满表格
#     tableView.horizontalHeader().setStretchLastSection(True)
#     # 水平方向，表格大小拓展到适当的尺寸
#     tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
#     # tableView.setEnabled(False)  #设置表格不可编
#
#     #标题背景模块
#     label = QtWidgets.QLabel()
#     label.setEnabled(True)
#     sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
#     sizePolicy.setHorizontalStretch(0)
#     sizePolicy.setVerticalStretch(5)
#     sizePolicy.setHeightForWidth(label.sizePolicy().hasHeightForWidth())
#     label.setSizePolicy(sizePolicy)
#     label.setObjectName("label")
#     gridLayout.addWidget(label, 1, 1, 2, 4)
#
#
#     return gridLayout
class view(QWidget):
    def write(self,i,all_content,model,key):
        item1 = QStandardItem(all_content['student'][key]['Sno'])
        item1.setEditable(False)  # 设置单元不可编辑
        item2 = QStandardItem(key)
        item2.setEditable(False)  # 设置单元不可编辑
        item3 = QStandardItem(all_content['student'][key]['age'])
        item3.setEditable(False)  # 设置单元不可编辑
        item4 = QStandardItem(all_content['student'][key]['sex'])
        item4.setEditable(False)  # 设置单元不可编辑
        item5 = QStandardItem(all_content['student'][key]['is'])
        item5.setEditable(False)  # 设置单元不可编辑
        item6 = QStandardItem(all_content['student'][key]['Course'])
        item6.setEditable(False)  # 设置单元不可编辑
        model.setItem(i, 0, item1)
        model.setItem(i, 1, item2)
        model.setItem(i, 2, item3)
        model.setItem(i, 3, item4)
        model.setItem(i, 4, item5)
        model.setItem(i, 5, item6)

    def hint(self,info,model):
        if model.rowCount() == 0:
            QMessageBox.information(self, '提示', '无该{}信息'.format(info))




    def type(self,comboBox,lineEdit,file,model):
        i = 0
        all_content = json.loads(files.basic_file_read(file))
        print("com=",comboBox)

            #全部查找
        if comboBox == 0:
            for key in all_content['student'].keys():
                self.write(i,all_content,model,key)
                i += 1
            self.hint('',model)
            pass
            # 按学号查找
        if comboBox == 1:
            for key in all_content['student'].keys():
                if all_content['student'][key]['Sno'] == lineEdit.text():
                    self.write(i,all_content,model,key)
                    i += 1
            self.hint("学号",model)
            pass
            # 按姓名查找
        if comboBox == 2:
            for key in all_content['student'].keys():
                if key == lineEdit.text():
                    self.write(i,all_content,model,key)
                    i += 1
            self.hint("姓名", model)
            pass
            # 按专业查找
        if comboBox == 3:
            for key in all_content['student'].keys():
                if all_content['student'][key]['is'] == lineEdit.text():
                    self.write(i, all_content, model, key)
                    i += 1
            self.hint("专业", model)
            pass
            # 按课程名查找
        if comboBox == 4:
            for key in all_content['student'].keys():
                if all_content['student'][key]['Course'] == lineEdit.text():
                    self.write(i, all_content, model, key)
                    i += 1
            self.hint("课程名", model)
            pass



