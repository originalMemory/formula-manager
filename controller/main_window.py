# coding=utf-8
"""
@project : formula-manager
@ide     : PyCharm
@file    : main_window
@author  : illusion
@desc    : 
@create  : 2021/8/8 4:49 下午:58
"""
from PyQt5.QtWidgets import QMainWindow

from ui.main_window import Ui_MainWindow


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
