# coding=utf-8
"""
@project : formula-manager
@ide     : PyCharm
@file    : db_helper
@author  : illusion
@desc    : 
@create  : 2021/8/6 1:46 下午:18
"""

import PyQt5
import sqlite3


class DBHelper:
    def __init__(self):
        super().__init__()
        self.conn = sqlite3.connect('database.db')
        self._create_tab_if_need()

    def _create_tab_if_need(self):
        c = self.conn.cursor()
        c.execute('''
        CREATE TABLE if not exists formula (
          id INT PRIMARY KEY NOT NULL,
          color_num TEXT,
          color_name TEXT,
          quality TEXT,
          dyes TEXT,
          catalyzers TEXT,
          create_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
          update_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        c.execute('''
        CREATE TABLE if not exists custom (
          id INT PRIMARY KEY NOT NULL,
          formula_ids TEXT,
          create_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
          update_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        ''')


db_helper = DBHelper()

if __name__ == '__main__':
    helper = DBHelper()
