# coding=utf-8
"""
@project : formula-manager
@ide     : PyCharm
@file    : custom_view
@author  : illusion
@desc    : 
@create  : 2021/8/13 5:49 下午:42
"""
from PyQt5.QtWidgets import QWidget

from ui.custom import Ui_Custom


class CustomView(QWidget, Ui_Custom):
    def __init__(self, parent=None):
        super(CustomView, self).__init__(parent)
        self.setupUi(self)
