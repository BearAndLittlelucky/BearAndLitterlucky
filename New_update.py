#!/usr/bin/env python
# _*_encoding: utf-8_*_
'''
@author: 小熊与小幸的故事
@license: (C) Copyright 2020-, Node Supply Chain Manager Corporation Limited.
@file: New_update.py
@time: 2020/10/2 16:48
@desc:
'''
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import json
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import IMS.FileOperation as files



class Ui_Form(QWidget):
    def setupUi(self, Form,file,index,tableWidget,sel):
        self.file = file
        self.index = index
        self.sel = sel
        self.tableWidget = tableWidget
        Form.setObjectName("Form")
        Form.resize(451, 532)
        Form.setWindowModality(Qt.ApplicationModal)  # disable parent window
        Form.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)  # 可最小化和关闭
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(40, 10, 371, 61))
        self.widget.setObjectName("widget")


        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 30, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        #姓名模块
        self.label_8 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(50, 0))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setValidator(self.rx(1))
        self.lineEdit_3.setPlaceholderText('请输入名字')  ##
        self.horizontalLayout.addWidget(self.lineEdit_3)

        #学号模块
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(40, 80, 371, 78))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 30, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_9 = QtWidgets.QLabel(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_2.addWidget(self.label_9)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setValidator(self.rx(0))
        self.lineEdit_4.setPlaceholderText('请输入学号（10位数字）')  ##
        self.horizontalLayout_2.addWidget(self.lineEdit_4)

        self.widget2 = QtWidgets.QWidget(Form)
        self.widget2.setGeometry(QtCore.QRect(40, 380, 371, 135))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_6.setContentsMargins(0, 50, 0, 50)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton = QtWidgets.QPushButton(self.widget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 28))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_6.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_6.addWidget(self.pushButton_2)


        #性别模块
        self.widget3 = QtWidgets.QWidget(Form)
        self.widget3.setGeometry(QtCore.QRect(40, 160, 371, 81))
        self.widget3.setObjectName("widget3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout_3.setContentsMargins(0, 30, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.widget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.radioButton = QtWidgets.QRadioButton(self.widget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.radioButton.sizePolicy().hasHeightForWidth())
        self.radioButton.setSizePolicy(sizePolicy)
        self.radioButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_3.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.radioButton_2.sizePolicy().hasHeightForWidth())
        self.radioButton_2.setSizePolicy(sizePolicy)
        self.radioButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_3.addWidget(self.radioButton_2)


        #年龄模块
        self.widget4 = QtWidgets.QWidget(Form)
        self.widget4.setGeometry(QtCore.QRect(40, 300, 371, 81))
        self.widget4.setObjectName("widget4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget4)
        self.horizontalLayout_4.setContentsMargins(0, 30, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.widget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.comboBox = QtWidgets.QComboBox(self.widget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setEditable(True)  # 可编辑
        self.comboBox.addItems(['', 'YY', 'BG', 'MM', 'DK', 'CH'])
        self.horizontalLayout_4.addWidget(self.comboBox)


        #专业模块
        self.widget5 = QtWidgets.QWidget(Form)
        self.widget5.setGeometry(QtCore.QRect(40, 240, 371, 61))
        self.widget5.setObjectName("widget5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget5)
        self.horizontalLayout_5.setContentsMargins(0, 30, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.widget5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.comboBox_2 = QtWidgets.QComboBox(self.widget5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        self.comboBox_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.setEditable(True)  # 可编辑
        self.comboBox_2.addItems(['', "18", "19", "20", '21', '22', '23', '24', '25', '26', '27'])
        self.horizontalLayout_5.addWidget(self.comboBox_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "{}信息".format('修改' if self.sel == 0 else '添加')))
        self.label_8.setText(_translate("Form", "姓名"))
        self.label_9.setText(_translate("Form", "学号"))
        self.pushButton.setText(_translate("Form", "{}".format('修改' if self.sel == 0 else '添加')))
        self.pushButton_2.setText(_translate("Form", "取消"))
        self.label.setText(_translate("Form", "性别"))
        self.radioButton.setText(_translate("Form", "男"))
        self.radioButton_2.setText(_translate("Form", "女"))
        self.label_2.setText(_translate("Form", "专业"))
        self.label_3.setText(_translate("Form", "年龄"))
        if self.sel == 0:
            self.write()  #填充需要修改的原信息
            self.pushButton.clicked.connect(lambda :self.change(Form))
        elif self.sel == 1:
            self.pushButton.clicked.connect(lambda: self.xiugai(Form))
        self.pushButton_2.clicked.connect(lambda: Form.close())  # 关闭修改信息窗口

    def write(self):
        all_content = json.loads(files.basic_file_read(self.file))
        for key in all_content['student'].keys():
            if key == self.index:
                self.lineEdit_3.setText(key)

                self.lineEdit_4.setText(all_content['student'][key]['Sno'])

                if all_content['student'][key]['sex'] == '男':
                    self.radioButton.setChecked(True)
                else:
                    self.radioButton_2.setChecked(True)

                self.comboBox.setCurrentText(all_content['student'][key]['is'])

                self.comboBox_2.setCurrentText(all_content['student'][key]['age'])

    def change(self,Form):
        repy = QMessageBox.warning(self, "修改提示", "是否确定修改？", QMessageBox.Yes | QMessageBox.No)
        if repy == QMessageBox.Yes:
            #删除原有信息
            with open(self.file, 'r', encoding='utf-8') as allstus:
                content = json.load(allstus)
                for key in list(content['student'].keys()):
                    if key == self.index:
                        del content['student'][key]
            with open(self.file, 'w', encoding='utf-8') as allstus:
                json.dump(content, allstus, ensure_ascii=False)
            # 写入新信息
            self.xiugai(Form)
        elif repy == QMessageBox.No:
            return

    # 写入修改信息或新增信息
    def xiugai(self,Form):
        # 判断必填项不为空
        if not self.lineEdit_3.text():
            QMessageBox.information(self, '提示', '姓名不可为空')
            return
        if not self.lineEdit_4.text():
            QMessageBox.information(self, '提示', '学号不可为空')
            return
        if not self.radioButton.isChecked() and not self.radioButton_2.isChecked():
            QMessageBox.information(self, '提示', '性别不可为空')
            return

        if not self.comboBox.currentText():
            QMessageBox.information(self, '提示', '年龄不可为空')
            return
        if not self.comboBox_2.currentText():
            QMessageBox.information(self, '提示', '专业不可为空')
            return
        # 判断是否已存在对应信息
        all_content = json.loads(files.basic_file_read(self.file))
        for key in all_content['student'].keys():
            if self.lineEdit_3.text() == key:
                QMessageBox.information(self, '提示', '已有该姓名，请重新填写')
                self.lineEdit_3.setText('')
                return
            elif self.lineEdit_4.text() == all_content['student'][key]['Sno']:
                QMessageBox.information(self, '提示', '已有该学号，请重新填写')
                self.lineEdit_4.setText('')
                return
        # 新增信息
        with open(self.file, 'r', encoding='utf-8') as addstus:
            content = json.load(addstus)
            content['student'][self.lineEdit_3.text()] = {'Sno': str(self.lineEdit_4.text()),
                                                          'age': self.comboBox_2.currentText(),
                                                          'sex': self.radioButton.text() if self.radioButton.isChecked() else self.radioButton_2.text(),
                                                          'is': self.comboBox.currentText(),
                                                          'Course': ''}
        # 转换为json格式
        with open(self.file, 'w', encoding='utf-8') as f:
            json.dump(content, f, ensure_ascii=False)  # ensure_ascii=False:转换时保持中文显示
        QMessageBox.information(self, '提示', '{}成功'.format('修改' if self.sel == 0 else '添加'))
        Form.close()  # 关闭当前窗口
        self.tableWidget.setRowCount(0)  # 清空列表

    # 输入规则
    def rx(self, n):
        if n == 1:
            # 正则表达式：中文和字母
            reg = QRegExp('[a-zA-Z\u4e00-\u9fa5]+$')
        else:
            # 正则表达式：10位数字
            reg = QRegExp('[0-9_]{10}')
        validator = QRegExpValidator()
        validator.setRegExp(reg)
        return validator


if __name__ == "__main__":
    App = QApplication(sys.argv)
    form = QWidget()
    MainWindow = Ui_Form().setupUi(form,'','')
    form.show()
    sys.exit(App.exec_())



