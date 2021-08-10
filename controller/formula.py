# coding=utf-8
"""
@project : formula-manager
@ide     : PyCharm
@file    : formula
@author  : illusion
@desc    : 配方管理页
@create  : 2021/8/8 5:17 下午:16
"""
import math
from functools import partial

from PyQt5.QtCore import QRegExp, QAbstractListModel, QModelIndex
from PyQt5.QtGui import QDoubleValidator, QStandardItemModel
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
        self.pushButtonFormulaDel.clicked.connect(self._del_formula)
        self.pushButtonFormulaEdit.clicked.connect(self._update_formula)
        self.pushButtonFormulaSearch.clicked.connect(self._search_formula)
        self.pushButtonPrePage.clicked.connect(partial(self._change_page, -1))
        self.pushButtonNextPage.clicked.connect(partial(self._change_page, 1))

        # 初始化数据
        self.formula_model = MyListModel(show_name='color_no')  # sql数据模型
        self.listViewFormula.setModel(self.formula_model)
        self.listViewFormula.selectionModel().currentChanged.connect(self._on_current_formula_change)
        self.page_index = 0  # 当前所在页
        self.page_size = 200  # 每页数据量
        self.count = 0  # 总数
        # 查询语句，返回项即为表格中列。left join 用于多表联查，where 1=1无意义，仅便于后续添加查询条件
        self.query_sql = 'select * from formula where 1=1 '
        self.where_sql = ''  # 条件语句
        self.count_sql = 'select count(*) from formula where 1=1 '  # 获取数据总数语句
        self._load_formula()

        # 初始化染料和催化剂
        self.dye_model = QStandardItemModel()
        self.dye_model.setHorizontalHeaderLabels(['名称', '数量'])
        self.tableViewDye.setModel(self.dye_model)
        self.catalyzer_model = QStandardItemModel()
        self.catalyzer_model.setHorizontalHeaderLabels(['名称', '数量'])
        self.tableViewCatalyzer.setModel(self.catalyzer_model)

    def _add_formula(self):
        color_no = self.lineEditColorNo.text()
        color_name = self.lineEditColorName.text()
        quality = self.lineEditQuality.text()
        if not color_no:
            QMessageBox.information(self, "提示", "未输入色号！", QMessageBox.Ok)
            return
        db_helper.insert_formula(color_no=color_no, color_name=color_name, quality=quality, dyes='', catalyzers='')
        self._load_formula()

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
        self._load_formula()

    def _search_formula(self):
        self.where_sql = ''
        color_no = self.lineEditColorNo.text()
        if color_no:
            self.where_sql = f"AND color_no LIKE '%{color_no}%'"
        color_name = self.lineEditColorName.text()
        if color_name:
            self.where_sql = f"AND color_name LIKE '%{color_name}%'"
        quality = self.lineEditQuality.text()
        if quality:
            self.where_sql = f"AND quality LIKE '%{quality}%'"
        self.page_index = 0
        self._load_formula()

    def _load_formula(self):
        self.count = db_helper.get_table_count(self.count_sql + self.where_sql)
        formulas = db_helper.execute_all(self.query_sql + self.where_sql)
        self.formula_model.clear()
        self.formula_model.add_items(formulas)

    def _load_dye_and_catalyzer(self):
        self.dye_model = QStandardItemModel()

    def _change_page(self, value):
        self.page_index += value
        if self.page_index < 0:
            self.page_index = 0
            return
        max_page = math.ceil(self.count / self.page_size)
        if self.page_index >= max_page:
            self.page_index = max_page - 1
        self.labelPage.setText(str(self.page_index + 1))
        self._load_formula()

    # region

    def _add_dye(self):
        name = self.lineEditDyeName.text()
        num = self.lineEditDyeNum.text()
        if not name or not num:
            QMessageBox('提示', '染料名称或数量不能为空！', QMessageBox.Ok)
            return

    def _on_current_formula_change(self, current: QModelIndex, previous: QModelIndex):
        """
        图片列表当前行变化事件
        :param current: 当前行索引
        :param previous:
        :return:
        """
        formula = self.formula_model.get_item(current.row())
        self.dyes = [x.split(';') for x in formula['dyes'].split('\n')]
        self.catalyzers = [x.split(';') for x in formula['catalyzers'].split('\n')]

    # endregion
