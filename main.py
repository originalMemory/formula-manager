# coding=utf-8
"""
@project : formula-manager
@ide     : PyCharm
@file    : main
@author  : illusion
@desc    : 
@create  : 2021/8/8 4:47 下午:07
"""

import sys

from PyQt5.QtWidgets import QApplication

import db_helper
from controller.main_window import MyMainWindow

if __name__ == '__main__':
    # 初始化qt
    app = QApplication(sys.argv)
    w = MyMainWindow()
    w.show()
    # w.login()

    sys.exit(app.exec_())
