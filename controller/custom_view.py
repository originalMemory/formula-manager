# coding=utf-8
"""
@project : formula-manager
@ide     : PyCharm
@file    : custom_view
@author  : illusion
@desc    : 
@create  : 2021/8/13 5:49 下午:42
"""
from functools import partial

import math
from PyQt5.QtCore import QModelIndex
from PyQt5.QtWidgets import QWidget, QMessageBox

from db_helper import db_helper
from model.custom import Custom
from model.formula import Formula
from model.formula_list_model import FormulaListModel
from model.my_list_model import MyListModel
from ui.custom import Ui_Custom


class CustomListModel(MyListModel):
    def _get_display_role(self, row):
        return self._data_list[row].name


class CustomView(QWidget, Ui_Custom):
    def __init__(self, parent=None):
        super(CustomView, self).__init__(parent)
        self.setupUi(self)

        # 关联事件
        self.pushButtonCustomAdd.clicked.connect(self._add_custom)
        self.pushButtonCustomDel.clicked.connect(self._del_custom)
        self.pushButtonCustomEdit.clicked.connect(self._update_custom)
        self.pushButtonCustomSearch.clicked.connect(self._search_custom)
        self.pushButtonAllColorNoSearch.clicked.connect(self._search_all_formula)
        self.pushButtonCustomColorNoSearch.clicked.connect(self._load_custom_formula)
        self.pushButtonCustomFormulaAdd.clicked.connect(self._add_custom_formula)
        self.pushButtonCustomFormulaDel.clicked.connect(self._del_custom_formula)
        self.lineEditAllColorNoFilter.returnPressed.connect(self._search_all_formula)
        self.lineEditCustomColorNoFilter.returnPressed.connect(self._load_custom_formula)
        self.pushButtonPrePage.clicked.connect(partial(self._change_page, -1))
        self.pushButtonNextPage.clicked.connect(partial(self._change_page, 1))

        # 加载数据
        self.custom_model = CustomListModel()
        self.custom_index = -1
        self.listViewCustom.setModel(self.custom_model)
        self.listViewCustom.selectionModel().currentChanged.connect(self._on_current_custom_change)
        self._load_custom(name_filter='')

        self.page_index = 0  # 当前所在页
        self.page_size = 200  # 每页数据量
        self.all_formula_model = FormulaListModel()
        self.listViewAllFormula.setModel(self.all_formula_model)
        self.custom_formula_ids = []
        self.custom_formula_model = FormulaListModel()
        self.listViewCustomFormula.setModel(self.custom_formula_model)
        self._load_all_formula()

    def _load_custom(self, name_filter):
        self.custom_index = -1
        self.custom_model.clear()
        customs = db_helper.search_custom(name_filter)
        self.custom_model.add_items(customs)

    def _on_current_custom_change(self, current: QModelIndex, previous: QModelIndex):
        """
        客户列表当前行变化事件
        :param current: 当前行索引
        :param previous:
        :return:
        """
        self.custom_index = current.row()
        self._update_detail_ui_on_custom_change()

    def _update_detail_ui_on_custom_change(self):
        custom = self.custom_model.get_item(self.custom_index)
        name = custom.name
        self.lineEditCustomName.setText(name)
        self.lineEditCustomColorNoFilter.setText('')
        self.custom_formula_ids = list(custom.formula_ids)
        self.lineEditCustomColorNoFilter.clear()
        self._load_custom_formula()
        self._load_all_formula()

    def _add_custom(self):
        name = self.lineEditCustomName.text()
        if not name:
            QMessageBox.information(self, "提示", "未输入客户名称！", QMessageBox.Ok)
            return
        db_helper.insert_custom(name)
        new = db_helper.select_last_item('custom')
        self.custom_model.add_item(Custom.from_dict(new))
        self.listViewCustom.setCurrentIndex(self.custom_model.index(self.custom_model.rowCount() - 1))

    def _update_custom(self):
        name = self.lineEditCustomName.text()
        if not name:
            QMessageBox.information(self, "提示", "未输入客户名称！", QMessageBox.Ok)
            return
        if self.custom_index < 0:
            QMessageBox.information(self, "提示", "未选择用户！", QMessageBox.Ok)
            return
        custom = self.custom_model.get_item(self.custom_index)
        db_helper.update_custom(item_id=custom.custom_id, name=name, formula_ids=self.custom_formula_ids)
        custom.name = name
        custom.formula_ids = self.custom_formula_ids
        self.custom_model.update_item(self.custom_index, custom)

    def _del_custom(self):
        if self.custom_index < 0:
            QMessageBox.information(self, "提示", "未选择用户！", QMessageBox.Ok)
            return
        custom = self.custom_model.get_item(self.custom_index)
        db_helper.delete('custom', [str(custom.custom_id)])
        self.custom_model.delete_item(self.custom_index)
        if self.custom_index >= self.custom_model.rowCount():
            row = self.custom_model.rowCount() - 1
        else:
            row = self.custom_index
        self.listViewCustom.setCurrentIndex(self.custom_model.index(row))
        self._update_detail_ui_on_custom_change()

    def _search_custom(self):
        self._load_custom(self.lineEditCustomName.text())

    def _change_page(self, value):
        self.page_index += value
        if self.page_index < 0:
            self.page_index = 0
            QMessageBox.information(self, "提示", "已经是第1页了！", QMessageBox.Ok)
            return
        max_page = math.ceil(self.count / self.page_size)
        if max_page == 0:
            max_page = 1
        if self.page_index >= max_page:
            self.page_index = max_page - 1
            QMessageBox.information(self, "提示", "已经是最后1页了！", QMessageBox.Ok)
            return
        self._load_all_formula()

    def _search_all_formula(self):
        self.page_index = 0
        self._load_all_formula()

    def _load_all_formula(self):
        self.listViewAllFormula.clearSelection()
        self.all_formula_model.clear()

        sql = 'SELECT * FROM formula WHERE 1=1'
        color_no_filter = self.lineEditAllColorNoFilter.text()
        where_sql = ''
        if color_no_filter:
            where_sql += f" AND color_no like '%{color_no_filter}%'"
        if self.custom_formula_ids:
            exclude_ids = [str(x) for x in self.custom_formula_ids]
            where_sql += f' AND id not in ({",".join(exclude_ids)})'
        sql += where_sql + f" limit {self.page_size} offset {self.page_index * self.page_size}"
        res = db_helper.execute_all(sql)
        if res:
            formulas = [Formula.from_dict(x) for x in res]
            self.all_formula_model.set_items(formulas)

        self.count = db_helper.get_table_count('select count(*) from formula where 1=1 ' + where_sql)
        max_page = math.ceil(self.count / self.page_size)
        page_str = f'{self.page_index + 1}/{max_page}'
        self.labelPage.setText(page_str)

    def _load_custom_formula(self):
        self.listViewCustomFormula.clearSelection()
        self.custom_formula_model.clear()

        sql = 'SELECT * FROM formula WHERE 1=1'
        ids = [str(x) for x in self.custom_formula_ids]
        sql += f' AND id in ({",".join(ids)})'
        color_no_filter = self.lineEditCustomColorNoFilter.text()
        if color_no_filter:
            sql += f" AND color_no like '%{color_no_filter}%'"
        res = db_helper.execute_all(sql)
        if res:
            formulas = [Formula.from_dict(x) for x in res]
            self.custom_formula_model.set_items(formulas)

    def _add_custom_formula(self):
        select_rows = self.listViewAllFormula.selectionModel().selectedRows()
        if self.custom_index < 0:
            QMessageBox.information(self, "提示", "未选择用户！", QMessageBox.Ok)
            return
        if len(select_rows) == 0:
            return
        ids = []
        for i in range(len(select_rows)):
            index = select_rows[i]
            item = self.all_formula_model.get_item(index.row())
            ids.append(item.formula_id)
        self.custom_formula_ids += ids
        self._load_all_formula()
        self._load_custom_formula()

    def _del_custom_formula(self):
        select_rows = self.listViewCustomFormula.selectionModel().selectedRows()
        if self.custom_index < 0:
            QMessageBox.information(self, "提示", "未选择用户！", QMessageBox.Ok)
            return
        if len(select_rows) == 0:
            return
        for i in range(len(select_rows)):
            index = select_rows[i]
            item = self.custom_formula_model.get_item(index.row())
            self.custom_formula_ids.remove(item.formula_id)
        self._load_all_formula()
        self._load_custom_formula()
