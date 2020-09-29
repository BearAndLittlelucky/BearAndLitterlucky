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
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qtpy import QtWidgets
import IMS.FileOperation as files


class view(QWidget):
    def setupUi(self,file):
        self.file = file
        ##查找页面
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        # 输入栏
        self.lineEdit = QtWidgets.QLineEdit()
        self.lineEdit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 4, 1, 1, 2)
        # 查询按钮
        self.pushButton = QtWidgets.QPushButton()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("查找")
        self.gridLayout.addWidget(self.pushButton, 4, 4, 1, 1)
        self.pushButton.clicked.connect(lambda: self.upd())  # view().type(self.comboBox.currentIndex(), self.lineEdit, self.file,self.model)
        # 选择查询方式
        self.comboBox = QtWidgets.QComboBox()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(["查找全部", "按学号查找", "按姓名查找", "按专业查找", "按课程名查找"])
        self.comboBox.currentIndexChanged.connect(lambda: self.sel())
        self.gridLayout.addWidget(self.comboBox, 4, 3, 1, 1)
        # 显示模块
        self.tableView = QtWidgets.QTableView()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 5, 1, 1, 4)

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Sno', 'Name', 'Age', "Sex", "Is", "Course"])
        self.tableView.setModel(self.model)
        # 水平方向标签拓展剩下的窗口部分，填满表格
        self.tableView.horizontalHeader().setStretchLastSection(True)
        # 水平方向，表格大小拓展到适当的尺寸
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # tableView.setEnabled(False)  #设置表格不可编

        # 标题背景模块
        self.label = QtWidgets.QLabel()
        self.label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        pix = QPixmap('D:\Project\IMS\软件界面\查找11.jpg')
        self.label.setPixmap(pix)
        # self.label.setStyleSheet("border: 2px solid red")
        self.label.setScaledContents(True)
        self.gridLayout.addWidget(self.label, 1, 1, 2, 4)

        return self.gridLayout



    def write(self,i,all_content,key):
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
        self.model.setItem(i, 0, item1)
        self.model.setItem(i, 1, item2)
        self.model.setItem(i, 2, item3)
        self.model.setItem(i, 3, item4)
        self.model.setItem(i, 4, item5)
        self.model.setItem(i, 5, item6)

    def hint(self,info):
        if self.model.rowCount() == 0:
            QMessageBox.information(self, '提示', '无该{}信息'.format(info))

    def upd(self):
        if self.model.rowCount() != 0:
            for i in range(self.model.rowCount()):
                self.model.removeRow(0)
        self.type()

    def sel(self):
        print("sel",self.comboBox.currentIndex())
        print("sel-text", self.comboBox.currentText())
        print("line",self.lineEdit.text())
        if self.comboBox.currentIndex() == 0:
            self.lineEdit.setEnabled(False)
        else:
            self.lineEdit.setEnabled(True)


    def type(self):
        i = 0
        all_content = json.loads(files.basic_file_read(self.file))
        print("com=",self.comboBox.currentIndex())

            #全部查找
        if self.comboBox.currentIndex() == 0:
            for key in all_content['student'].keys():
                self.write(i,all_content,key)
                i += 1
            self.hint('')
            pass
            # 按学号查找
        if self.comboBox.currentIndex() == 1:
            for key in all_content['student'].keys():
                if all_content['student'][key]['Sno'] == self.lineEdit.text():
                    self.write(i,all_content,key)
                    i += 1
            self.hint("学号")
            pass
            # 按姓名查找
        if self.comboBox.currentIndex() == 2:
            for key in all_content['student'].keys():
                if key == self.lineEdit.text():
                    self.write(i,all_content,key)
                    i += 1
            self.hint("姓名")
            pass
            # 按专业查找
        if self.comboBox.currentIndex() == 3:
            for key in all_content['student'].keys():
                if all_content['student'][key]['is'] == self.lineEdit.text():
                    self.write(i, all_content, key)
                    i += 1
            self.hint("专业")
            pass
            # 按课程名查找
        if self.comboBox.currentIndex() == 4:
            for key in all_content['student'].keys():
                if all_content['student'][key]['Course'] == self.lineEdit.text():
                    self.write(i, all_content, key)
                    i += 1
            self.hint("课程名")
            pass



