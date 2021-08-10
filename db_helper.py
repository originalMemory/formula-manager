# coding=utf-8
"""
@project : formula-manager
@ide     : PyCharm
@file    : db_helper
@author  : illusion
@desc    : 
@create  : 2021/8/6 1:46 下午:18
"""
import os

import PyQt5
import sqlite3


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class DBHelper:
    def __init__(self):
        super().__init__()
        db_path = 'database.db'
        exist_db = os.path.exists(db_path)
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = dict_factory
        if not exist_db:
            self._create_tab()

    def _create_tab(self):
        self.execute_one('''
        CREATE TABLE if not exists formula (
          id INTEGER PRIMARY KEY,
          color_no TEXT,
          color_name TEXT,
          quality TEXT,
          dyes TEXT,
          catalyzers TEXT,
          create_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
          update_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        self.execute_one('''
        CREATE TABLE if not exists custom (
          id INTEGER PRIMARY KEY,
          formula_ids TEXT,
          create_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
          update_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        ''')

    def execute_one(self, sql):
        c = self.conn.cursor()
        try:
            result = c.execute(sql)
            return result.fetchone()
        except sqlite3.Error as error:
            print(f'数据库错误：{error}')
        finally:
            c.close()
            self.conn.commit()

    def execute_all(self, sql):
        c = self.conn.cursor()
        try:
            result = c.execute(sql)
            return result.fetchall()
        except sqlite3.Error as error:
            print(f'数据库错误：{error}')
        finally:
            c.close()
            self.conn.commit()

    def insert_formula(self, color_no, color_name, quality, dyes, catalyzers):
        if not color_name:
            color_name = ''
        if not quality:
            quality = ''
        if not dyes:
            dyes = ''
        if not catalyzers:
            catalyzers = ''
        res = self.execute_one(f"""
        INSERT INTO formula(color_no,color_name,quality,dyes,catalyzers)
        VALUES ('{color_no}','{color_name}','{quality}','{dyes}','{catalyzers}')
        """)
        return res is not None

    def update_formula(self, item_id, color_no, color_name, quality, dyes, catalyzers):
        if not color_name:
            color_name = ''
        if not quality:
            quality = ''
        if not dyes:
            dyes = ''
        if not catalyzers:
            catalyzers = ''
        res = self.execute_one(f"""
        UPDATE formula SET color_no='{color_no}',color_name='{color_name}',quality='{quality}',dyes='{dyes}'
        ,catalyzers='{catalyzers}' WHERE id={item_id}
        """)
        return res is not None

    def delete(self, table, ids):
        res = self.execute_one(f'DELETE FROM {table} WHERE id in ({",".join(ids)})')
        return res is not None

    def get_table_count(self, sql):
        res = self.execute_one(sql)
        return res['count(*)']


db_helper = DBHelper()

if __name__ == '__main__':
    helper = DBHelper()
