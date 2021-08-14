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

from common_helper import CommonHelper
from controller.custom_view import CustomView
from controller.export_view import ExportView
from controller.formula_view import FormulaView
from ui.main_window import Ui_MainWindow


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        # 创建功能区
        self.formula = FormulaView()
        self.custom = CustomView()
        self.export = ExportView()

        self.init_window()
        self.listWidget.currentRowChanged.connect(self.display)

        # 加载界面qss文件，美化界面
        CommonHelper.load_qss(self.listWidget, 'left.qss')
        CommonHelper.load_qss(self, 'main.qss')

    def init_window(self):
        # 创建窗口界面
        self.listWidget.insertItem(0, '配方管理')
        self.stackedWidget.addWidget(self.formula)
        self.listWidget.insertItem(1, '客户管理')
        self.stackedWidget.addWidget(self.custom)
        self.listWidget.insertItem(1, '导出管理')
        self.stackedWidget.addWidget(self.export)

        # 默认显示第一个项目
        self.listWidget.setCurrentRow(0)
        self.stackedWidget.setCurrentIndex(2)

    def display(self, i):
        """
        显示选中的功能界面
        :param i: 功能界面索引
        :return:
        """
        # 设置当前可见的选项的索引。因为StackedWidget默认有两个控件，所以索引使用时需要+2
        self.stackedWidget.setCurrentIndex(i + 2)

