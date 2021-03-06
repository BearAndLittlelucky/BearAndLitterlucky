# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import IMS.LoginIn1
import IMS.Delete
import IMS.View
import IMS.Add
import IMS.View_sql



class Ui_Form(QWidget):
    def __init__(self,file):
        super(Ui_Form,self).__init__()
        self.setupUi(self,file)

    def setupUi(self, Form,file):
        self.file = file
        Form.setObjectName("Form")
        Form.resize(1205, 686)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMaximumSize(QtCore.QSize(197, 16777215))

        self.listWidget.setStyleSheet("QListWidget{background-color:#FFFFF0;color:rgb(200,200,200);border:2px solid PaleGreen;border-radius: 4px;}" # listwidget背景样式
                                      "QListWidget:Item{padding-top:15px; padding-bottom:15px;}" # 字体上下空白大小
                                      "QListWidget::Item:hover{background:PaleGreen; }" # 鼠标移动至Item时
                                      "QListWidget::item:selected{background:LightGreen; color:DimGrey;}" # 选中时
                                      )
        # set listWidget item style
        View_sql = QListWidgetItem(QIcon("D:\Project\IMS\\frequency.ico"),'学生基本信息(MySQL版)')
        View = QListWidgetItem(QIcon("D:\Project\IMS\\frequency.ico"), '学生基本信息(json版)')
        continue2 = QListWidgetItem(QIcon("D:\Project\IMS\\frequency.ico"), 'continue2')
        continue3 = QListWidgetItem(QIcon("D:\Project\IMS\\frequency.ico"), 'continue3')
        self.listWidget.insertItem(0, View_sql)
        self.listWidget.insertItem(1, View)
        self.listWidget.insertItem(2, continue2)
        self.listWidget.insertItem(3, continue3)
        self.listWidget.currentRowChanged.connect(self.display)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_2.addWidget(self.listWidget)
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName("stackedWidget")



        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.page_3.setLayout(IMS.View_sql.view().setupUi())  #通过MySQL存储数据

        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_4.setLayout(IMS.View.view().setupUi(self.file)) #通过json存储数据

        self.page_5.setObjectName("page_5")
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_5.setLayout(IMS.Delete.Ui_Form().setupUi(self.file))

        self.page_6.setObjectName("page_6")
        self.stackedWidget.addWidget(self.page_6)
        self.page_6.setLayout(IMS.Delete.Ui_Form().setupUi(self.file))




        self.horizontalLayout_2.addWidget(self.stackedWidget)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Student information management system"))

    def display(self,index):
        self.stackedWidget.setCurrentIndex(index)



if __name__ == "__main__":
    App = QApplication(sys.argv)
    MainWindow = Ui_Form("D:\Project\IMS\\UserInfo\dzx.json")
    MainWindow.show()
    sys.exit(App.exec_())



