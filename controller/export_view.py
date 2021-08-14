#!/user/bin/env python3
# coding=utf-8
"""
@project : formula-manager
@ide     : PyCharm
@file    : export_view
@author  : illusion
@desc    : 
@create  : 2021/8/14
"""
from PyQt5.QtWidgets import QWidget

from ui.export import Ui_Export


class ExportView(QWidget, Ui_Export):
    def __init__(self, parent=None):
        super(ExportView, self).__init__(parent)
        self.setupUi(self)
