#!/user/bin/env python
# coding=utf-8
"""
@project : DeviceManager
@ide     : PyCharm
@file    : common_helper
@author  : wuhoubo
@desc    : 
@create  : 2019/9/10 0:57:11
@update  :
"""
import datetime
import os
import time

from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import QMessageBox
# from openpyxl import Workbook

import config


class CommonHelper:

    @staticmethod
    def load_qss(widget, filename):
        qss_path = os.path.join(config.cur_dir_path, 'css', filename)
        try:
            with open(qss_path, 'r') as f:
                widget.setStyleSheet(f.read())
        except Exception as e:
            print(e)

    @staticmethod
    def date_to_timezone_date(date, timezone=8):
        t = time.strptime(date, "%Y-%m-%d %H:%M:%S")
        timestamp = int(time.mktime(t))
        dt = datetime.datetime.fromtimestamp(timestamp).replace(tzinfo=datetime.timezone.utc)
        dt8 = dt.astimezone(datetime.timezone(datetime.timedelta(hours=timezone)))
        date = dt8.strftime("%Y-%m-%d %H:%M:%S")

        return date

    # @staticmethod
    # def export_excel(parent_widget, headers, filename, model):
    #     workbook = Workbook()
    #     sheet = workbook.active  # 获取当前活跃的sheet,默认是第一个sheet
    #
    #     # 设置列名
    #     sheet.append(headers)
    #
    #     row_count = model.rowCount()
    #     col_count = model.columnCount()
    #
    #     for row in range(row_count):
    #         for col in range(col_count):
    #             value = model.data(model.index(row, col))
    #             if isinstance(value, QDateTime):
    #                 value = value.toString("yyyy-MM-dd hh:mm:ss")
    #             else:
    #                 value = str(value)
    #             sheet.cell(row + 2, col + 1).value = value
    #
    #     export_dir = os.path.join(config.cur_dir_path, "export")
    #     if not os.path.exists(export_dir):
    #         os.makedirs(export_dir)
    #     export_file = os.path.join(export_dir, filename)
    #     try:
    #         if os.path.exists(export_file):
    #             os.remove(export_file)
    #         workbook.save(export_file)
    #         os.system("start explorer %s" % export_dir)
    #     except Exception as e:
    #         QMessageBox.information(parent_widget, "提示", str(e), QMessageBox.Ok)
