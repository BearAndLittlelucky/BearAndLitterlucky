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
from numpy.ma import count
import IMS.FileOperation as files
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import IMS.Update

##############################################################################
####???无返回值？？？？？
class EmptyDelegate(QItemDelegate):
    def __init__(self, parent):
        super(EmptyDelegate, self).__init__(parent)

    def createEditor(self, QWidget, QStyleOptionViewItem, QModelIndex):
        return None
################################################################################



class view(QWidget,QObject):
    sendmsg = pyqtSignal(str, str, str, str, str, str)
    def setupUi(self,file,listWidget):
        self.file = file
        self.listWidget = listWidget
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
        #设置整行选中
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)


        self.verticalLayout.addWidget(self.tableWidget)

        return self.verticalLayout


    def write(self, i, all_content, key):
        cell_widget = QWidget()
        horizontalLayout = QtWidgets.QHBoxLayout(cell_widget)
        locals()['but0'+str(i)] = QtWidgets.QPushButton("修改")
        locals()['but0'+str(i)].clicked.connect(lambda :self.change(i))
        locals()['but1'+str(i)] = QtWidgets.QPushButton("删除")
        locals()['but1'+str(i)].clicked.connect(lambda: self.dele(i))
        horizontalLayout.addWidget(locals()['but0'+str(i)])
        horizontalLayout.addWidget(locals()['but1'+str(i)])
        self.tableWidget.setRowHeight(i,50) # 设置每行高度
        self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(all_content['student'][key]['Sno']))
        self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(key))
        self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(all_content['student'][key]['age']))
        self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(all_content['student'][key]['sex']))
        self.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(all_content['student'][key]['is']))
        self.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(all_content['student'][key]['Course']))
        self.tableWidget.setItemDelegateForColumn(i, EmptyDelegate(self))  # 设置不可编辑????????
        self.tableWidget.setCellWidget(i, 6, cell_widget)

    def change(self,i):

        upde = IMS.Update.Ui_Form(self.file,
                                     self.tableWidget.item(i,1).text(),
                                     self.tableWidget.item(i,0).text(),
                                     self.tableWidget.item(i,2).text(),
                                     self.tableWidget.item(i,3).text(),
                                     self.tableWidget.item(i,4).text(),
                                     self.tableWidget.item(i,5).text())

        #upde.setupUi(form)
        #self.listWidget.setCurrentRow(2)


    # 删除学生信息的模块
    def dele(self,i):
        repy = QMessageBox.warning(self, "删除提示", "是否确定删除？", QMessageBox.Yes | QMessageBox.No)
        if repy == QMessageBox.No:
            return
        delstu_name = self.tableWidget.item(i,1).text()#获取某行某列item中的x信息)
        with open(self.file, 'r', encoding='utf-8') as allstus:
            content = json.load(allstus)
            for key in content['student'].keys():
                if key == delstu_name:
                    del content['student'][key]
                    QMessageBox.information(self, '提示', '删除成功')
                    self.tableWidget.setRowCount(0)
                    break
            else:
                QMessageBox.information(self, '提示', '未找到这名同学的信息')
        with open(self.file, 'w', encoding='utf-8') as allstus:
            json.dump(content, allstus,ensure_ascii=False)


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







