#!/usr/bin/env python
# _*_encoding: utf-8_*_
'''
@author: 小熊与小幸的故事
@license: (C) Copyright 2020-, Node Supply Chain Manager Corporation Limited.
@file: Uodate.py
@time: 2020/9/21 22:25
@desc:
'''
from PyQt5.QtWidgets import *

def Update():
    layout = QHBoxLayout()
    layout.addWidget(QLabel('科目'))
    layout.addWidget(QCheckBox('物理'))
    layout.addWidget(QCheckBox('高数'))
    return layout