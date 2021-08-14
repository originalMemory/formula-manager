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

from model.custom import Custom
from model.formula import Formula


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
        CREATE TRIGGER formula_update_trig
        AFTER UPDATE ON formula
        BEGIN
          update formula SET update_time = datetime('now') WHERE id = NEW.id;
        END;
        ''')
        self.execute_one('''
        CREATE TABLE if not exists custom (
          id INTEGER PRIMARY KEY,
          name TEXT,
          formula_ids TEXT,
          create_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
          update_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        self.execute_one('''
        CREATE TRIGGER custom_update_trig
        AFTER UPDATE ON custom
        BEGIN
          update custom SET update_time = datetime('now') WHERE id = NEW.id;
        END;
        ''')

    def execute_one(self, sql):
        c = self.conn.cursor()
        try:
            result = c.execute(sql)
            print(sql)
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
            print(sql)
            return result.fetchall()
        except sqlite3.Error as error:
            print(f'数据库错误：{error}')
        finally:
            c.close()
            self.conn.commit()

    def delete(self, table, ids):
        res = self.execute_one(f'DELETE FROM {table} WHERE id in ({",".join(ids)})')
        return res is not None

    def get_table_count(self, sql):
        res = self.execute_one(sql)
        return res['count(*)']

    def select_last_item(self, table):
        return self.execute_one(f'SELECT * FROM {table} WHERE id=last_insert_rowid()')

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

    def search_one_formula(self, formula_id):
        res = self.execute_one(f'SELECT * FROM formula WHERE id={formula_id}')
        if res:
            return Formula.from_dict(res)

    def search_formulas(self, ids=None, color_no_filter=None, exclude_ids=None, page=None, page_size=None):
        sql = 'SELECT * FROM formula WHERE 1=1'
        if ids is not None:
            ids = [str(x) for x in ids]
            sql += f' AND id in ({",".join(ids)})'
        if color_no_filter:
            sql += f" AND color_no like '%{color_no_filter}%'"
        if exclude_ids:
            exclude_ids = [str(x) for x in exclude_ids]
            sql += f' AND id not in ({",".join(exclude_ids)})'
        if page and page_size:
            sql += f" limit {page_size} offset {page * page_size}"
        res = self.execute_all(sql)
        if res:
            return [Formula.from_dict(x) for x in res]

    def insert_custom(self, name):
        if not name:
            return False
        self.execute_one(f"INSERT INTO custom(name,formula_ids) VALUES ('{name}','')")

    def update_custom(self, item_id, name, formula_ids):
        if not item_id or not name:
            return False
        formula_ids = [str(x) for x in formula_ids]
        formula_ids = ';'.join(formula_ids)
        res = self.execute_one(f"""
        UPDATE custom SET name='{name}',formula_ids='{formula_ids}' WHERE id={item_id}
        """)
        return res is not None

    def search_custom(self, name_filter):
        res = self.execute_all(f"SELECT * FROM custom WHERE name like '%{name_filter}%'")
        return [Custom.from_dict(x) for x in res]


db_helper = DBHelper()

if __name__ == '__main__':
    helper = DBHelper()
