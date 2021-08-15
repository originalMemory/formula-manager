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

