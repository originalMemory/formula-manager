# coding=utf-8
"""
@project : formula-manager
@ide     : PyCharm
@file    : formula
@author  : illusion
@desc    : 配方管理页
@create  : 2021/8/8 5:17 下午:16
"""
from PyQt5.QtCore import QRegExp, QAbstractListModel
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtWidgets import QWidget, QMessageBox

from db_helper import db_helper
from model.my_list_model import MyListModel
from ui.formula import Ui_Formula


class Formula(QWidget, Ui_Formula):
    def __init__(self, parent=None):
        super(Formula, self).__init__(parent)
        self.setupUi(self)

        # 限制只能输入数字和小数点
        validator = QDoubleValidator()
        self.lineEditDyeNum.setValidator(validator)
        self.lineEditCatalyzerNum.setValidator(validator)

        # 关联点击事件
        self.pushButtonFormulaAdd.clicked.connect(self._add_formula)

        # 初始化数据
        self.formula_model = MyListModel(show_name='color_no')  # sql数据模型
        self.listViewFormula.setModel(self.formula_model)
        self.page_index = 0  # 当前所在页
        self.page_size = 200  # 每页数据量
        self.count = 0  # 总数
        # 查询语句，返回项即为表格中列。left join 用于多表联查，where 1=1无意义，仅便于后续添加查询条件
        self.query_sql = 'select * from formula where 1=1 '
        self.where_sql = ''  # 条件语句
        self.count_sql = 'select count(*) from formula where 1=1 '  # 获取数据总数语句
        self.load_data()

    def _add_formula(self):
        color_no = self.lineEditColorNo.text()
        color_name = self.lineEditColorName.text()
        quality = self.lineEditQuality.text()
        if not color_no:
            QMessageBox.information(self, "提示", "未输入色号！", QMessageBox.Ok)
            return
        db_helper.insert_formula(color_no=color_no, color_name=color_name, quality=quality, dyes='', catalyzers='')
        self.load_data()

    def _del_formula(self):
        select_rows = self.listViewFormula.selectionModel().selectedRows()
        if len(select_rows) == 0:
            return
        ids = []
        for i in range(len(select_rows)):
            index = select_rows[i]
            item = self.formula_model.get_item(index.row() - i)
            ids.append(item['id'])
        db_helper.delete('formula', ids)

    def _update_formula(self):
        color_no = self.lineEditColorNo.text()
        color_name = self.lineEditColorName.text()
        quality = self.lineEditQuality.text()
        if not color_no:
            QMessageBox.information(self, "提示", "未输入色号！", QMessageBox.Ok)
            return
        db_helper.insert_formula(color_no=color_no, color_name=color_name, quality=quality, dyes='', catalyzers='')
        self.load_data()

    def load_data(self):
        self.count = db_helper.get_table_count(self.count_sql + self.where_sql)
        formulas = db_helper.execute_all(self.query_sql + self.where_sql)
        self.formula_model.clear()
        self.formula_model.add_items(formulas)
