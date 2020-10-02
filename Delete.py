#!/usr/bin/env python
# _*_encoding: utf-8_*_
'''
@author: 小熊与小幸的故事
@license: (C) Copyright 2020-, Node Supply Chain Manager Corporation Limited.
@file: Delete.py
@time: 2020/9/21 22:22
@desc:
'''
import json

from numpy.ma import count

import IMS.FileOperation as files
from PyQt5.QtGui import QPixmap, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets


##############################################################################
####???无返回值？？？？？
class EmptyDelegate(QItemDelegate):
    def __init__(self, parent):
        super(EmptyDelegate, self).__init__(parent)

    def createEditor(self, QWidget, QStyleOptionViewItem, QModelIndex):
        return None
################################################################################



class Ui_Form(QWidget):
    def setupUi(self,file):
        self.file = file
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        # 标题模块
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
        self.verticalLayout.addWidget(self.label)

        #操作查找模块
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setEnabled(False)
        self.horizontalLayout.addWidget(self.lineEdit)
        self.comboBox = QtWidgets.QComboBox()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(["查找全部", "按学号查找", "按姓名查找", "按专业查找", "按课程名查找"])
        self.comboBox.currentIndexChanged.connect(lambda: self.sel())
        self.horizontalLayout.addWidget(self.comboBox)
        self.pushButton = QtWidgets.QPushButton()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("查找")
        self.pushButton.clicked.connect(lambda: self.upd())
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        #显示模块
        self.tableWidget = QtWidgets.QTableWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(['Sno', 'Name', 'Age', "Sex", "Is", "Course",'action'])
        #水平拉伸
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)



        self.verticalLayout.addWidget(self.tableWidget)

        return self.verticalLayout


    def write(self, i, all_content, key):
        #if i > 1:
        #self.tableWidget.insertRow(1)
        cell_widget = QWidget()
        horizontalLayout = QtWidgets.QHBoxLayout(cell_widget)
        but = QtWidgets.QPushButton("修改")
        but.clicked.connect(lambda :self.change())
        but1 = QtWidgets.QPushButton("删除")
        but1.clicked.connect(lambda: self.dele())
        horizontalLayout.addWidget(but)
        horizontalLayout.addWidget(but1)
        self.tableWidget.setRowHeight(i,50) # 设置每行高度
        self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(all_content['student'][key]['Sno']))
        self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(key))
        self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(all_content['student'][key]['age']))
        self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(all_content['student'][key]['sex']))
        self.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(all_content['student'][key]['is']))
        self.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(all_content['student'][key]['Course']))
        self.tableWidget.setItemDelegateForColumn(i, EmptyDelegate(self))  # 设置不可编辑????????
        self.tableWidget.setCellWidget(i, 6, cell_widget)

    def change(self):
        print("修改")

    def dele(self):
        print("删除")


    def hint(self, info):
        if self.tableWidget.rowCount() == 0:
            QMessageBox.information(self, '提示', '无该{}信息'.format(info))
        pass

    def upd(self):
        if self.tableWidget.rowCount() != 0:
            self.tableWidget.setRowCount(0)
        self.type()

    def sel(self):
        print("sel", self.comboBox.currentIndex())
        print("sel-text", self.comboBox.currentText())
        print("line", self.lineEdit.text())
        if self.comboBox.currentIndex() == 0:
            self.lineEdit.setEnabled(False)
        else:
            self.lineEdit.setEnabled(True)

    def type(self):
        i = 0
        all_content = json.loads(files.basic_file_read(self.file))
        print("com=", self.comboBox.currentIndex())
        self.tableWidget.clearContents() # 清空表格中的内容（不包含表头）
        list_all = list(all_content['student'].values())  # 字典转换为列表

        # 全部查找
        if self.comboBox.currentIndex() == 0:
            self.tableWidget.setRowCount(count(list(all_content['student'].keys())))
            for key in all_content['student'].keys():
                self.write(i, all_content, key)
                i += 1
            self.hint('')
            pass
            # 按学号查找
        if self.comboBox.currentIndex() == 1:
            self.tableWidget.setRowCount(sum(item['Sno'] == self.lineEdit.text() for item in list_all))  #计算符合条件的个数以增加行数
            for key in all_content['student'].keys():
                if all_content['student'][key]['Sno'] == self.lineEdit.text():
                    self.write(i, all_content, key)
                    i += 1
            self.hint("学号")
            pass
            # 按姓名查找
        if self.comboBox.currentIndex() == 2:
            self.tableWidget.setRowCount(sum(key == self.lineEdit.text() for key in all_content['student'].keys()))  #计算符合条件的个数以增加行数
            for key in all_content['student'].keys():
                if key == self.lineEdit.text():
                    self.write(i, all_content, key)
                    i += 1
            self.hint("姓名")
            pass
            # 按专业查找
        if self.comboBox.currentIndex() == 3:
            self.tableWidget.setRowCount(sum(item['is'] == self.lineEdit.text() for item in list_all))  #计算符合条件的个数以增加行数
            for key in all_content['student'].keys():
                if all_content['student'][key]['is'] == self.lineEdit.text():
                    self.write(i, all_content, key)
                    i += 1
            self.hint("专业")
            pass
            # 按课程名查找
        if self.comboBox.currentIndex() == 4:
            self.tableWidget.setRowCount(sum(item['Course'] == self.lineEdit.text() for item in list_all))  # 计算符合条件的个数以增加行数
            for key in all_content['student'].keys():
                if all_content['student'][key]['Course'] == self.lineEdit.text():
                    self.write(i, all_content, key)
                    i += 1
            self.hint("课程名")
            pass




