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

from PyQt5.QtCore import QModelIndex
from PyQt5.QtGui import QDoubleValidator, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QMessageBox

from db_helper import db_helper
from model.formula import Formula, FormulaItem
from model.formula_list_model import FormulaListModel
from ui.formula import Ui_Formula


class FormulaView(QWidget, Ui_Formula):
    def __init__(self, parent=None):
        super(FormulaView, self).__init__(parent)
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
        self.pushButtonDyeAdd.clicked.connect(self._add_dye)
        self.pushButtonDyeDel.clicked.connect(self._del_dye)
        self.pushButtonDyeEdit.clicked.connect(self._update_dye)
        self.pushButtonDyeSearch.clicked.connect(self._search_dye)
        self.pushButtonCatalyzerAdd.clicked.connect(self._add_catalyzer)
        self.pushButtonCatalyzerDel.clicked.connect(self._del_catalyzer)
        self.pushButtonCatalyzerEdit.clicked.connect(self._update_catalyzer)
        self.pushButtonCatalyzerSearch.clicked.connect(self._search_catalyzer)

        # 初始化数据
        self.formula_model = FormulaListModel()  # 数据模型
        self.formula_index = -1
        self.listViewFormula.setModel(self.formula_model)
        self.listViewFormula.selectionModel().currentChanged.connect(self._on_current_formula_change)
        self.page_index = 0  # 当前所在页
        self.page_size = 200  # 每页数据量
        self.count = 0  # 总数
        # 查询语句，返回项即为表格中列。left join 用于多表联查，where 1=1无意义，仅便于后续添加查询条件
        self.query_sql = 'select * from formula where 1=1 '
        self.where_sql = ''  # 条件语句
        self._load_formula()

        # 初始化染料和催化剂
        self.dyes = []
        self.dye_index = -1
        self.dye_model = QStandardItemModel()
        self.tableViewDye.setModel(self.dye_model)
        self.tableViewDye.selectionModel().currentChanged.connect(self._on_current_dye_change)
        self._load_dye()
        self.catalyzers = []
        self.catalyzer_index = -1
        self.catalyzer_model = QStandardItemModel()
        self.tableViewCatalyzer.setModel(self.catalyzer_model)
        self.tableViewCatalyzer.selectionModel().currentChanged.connect(self._on_current_catalyzer_change)
        self._load_catalyzer()

    def _add_formula(self):
        color_no = self.lineEditColorNo.text()
        color_name = self.lineEditColorName.text()
        quality = self.lineEditQuality.text()
        if not color_no:
            QMessageBox.information(self, "提示", "未输入色号！", QMessageBox.Ok)
            return
        dyes = [x.to_str() for x in self.dyes]
        dyes = '\n'.join(dyes)
        catalyzers = [x.to_str() for x in self.catalyzers]
        catalyzers = '\n'.join(catalyzers)
        db_helper.insert_formula(color_no=color_no, color_name=color_name, quality=quality, dyes=dyes,
                                 catalyzers=catalyzers)
        self._load_formula()
        self._clear_cur()

    def _clear_cur(self):
        self.formula_index = -1
        self.dye_index = -1
        self.catalyzer_index = -1
        self.lineEditColorNo.clear()
        self.lineEditColorName.clear()
        self.lineEditQuality.clear()
        self.lineEditDyeName.clear()
        self.lineEditDyeNum.clear()
        self.lineEditCatalyzerName.clear()
        self.lineEditCatalyzerNum.clear()
        self.dyes.clear()
        self.catalyzers.clear()
        self._load_dye()
        self._load_catalyzer()

    def _del_formula(self):
        select_rows = self.listViewFormula.selectionModel().selectedRows()
        if len(select_rows) == 0:
            return
        ids = []
        for i in range(len(select_rows)):
            index = select_rows[i]
            item = self.formula_model.delete_item(index.row() - i)
            ids.append(str(item.formula_id))
        db_helper.delete('formula', ids)
        self._load_formula()
        self._clear_cur()

    def _update_formula(self):
        if self.formula_index < 0 or self.formula_index >= self.formula_model.rowCount():
            QMessageBox.information(self, "提示", "未选择配方，无法更新！", QMessageBox.Ok)
            return
        color_no = self.lineEditColorNo.text()
        if not color_no:
            QMessageBox.information(self, "提示", "未输入色号！", QMessageBox.Ok)
            return
        formula = self.formula_model.get_item(self.formula_index)
        color_name = self.lineEditColorName.text()
        quality = self.lineEditQuality.text()
        dyes = [x.to_str() for x in self.dyes]
        dyes = '\n'.join(dyes)
        catalyzers = [x.to_str() for x in self.catalyzers]
        catalyzers = '\n'.join(catalyzers)
        db_helper.update_formula(item_id=formula.formula_id, color_no=color_no, color_name=color_name, quality=quality,
                                 dyes=dyes, catalyzers=catalyzers)
        new_formula = db_helper.search_one_formula(formula.formula_id)
        self.formula_model.update_item(self.formula_index, new_formula)

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
        self.dyes.clear()
        self.catalyzers.clear()
        self._load_dye()
        self._load_catalyzer()

        self._load_formula()

    def _load_formula(self):
        page_sql = f" limit {self.page_size} offset {self.page_index * self.page_size}"
        sql = self.query_sql + self.where_sql + page_sql
        formulas = db_helper.execute_all(sql)
        formulas = [Formula.from_dict(x) for x in formulas]
        self.formula_model.clear()
        self.formula_model.add_items(formulas)

        self.count = db_helper.get_table_count('select count(*) from formula where 1=1 ' + self.where_sql)
        max_page = math.ceil(self.count / self.page_size)
        if max_page == 0:
            max_page = 1
        page_str = f'{self.page_index + 1}/{max_page}'
        self.labelPage.setText(page_str)

    def _change_page(self, value):
        self.page_index += value
        if self.page_index < 0:
            self.page_index = 0
            QMessageBox.information(self, "提示", "已经是第1页了！", QMessageBox.Ok)
            return
        max_page = math.ceil(self.count / self.page_size)
        if self.page_index >= max_page:
            self.page_index = max_page - 1
            QMessageBox.information(self, "提示", "已经是最后1页了！", QMessageBox.Ok)
            return
        self._load_formula()

    def _on_current_formula_change(self, current: QModelIndex, previous: QModelIndex):
        """
        图片列表当前行变化事件
        :param current: 当前行索引
        :param previous:
        :return:
        """
        index = current.row()
        self.formula_index = index
        formula = self.formula_model.get_item(index)
        self.lineEditColorNo.setText(formula.color_no)
        self.lineEditColorName.setText(formula.color_name)
        self.lineEditQuality.setText(formula.quality)
        self.dyes = list(formula.dyes)
        self.catalyzers = list(formula.catalyzers)
        self.lineEditDyeName.clear()
        self.lineEditDyeNum.clear()
        self.lineEditCatalyzerName.clear()
        self.lineEditCatalyzerNum.clear()
        self._load_dye()
        self._load_catalyzer()

    # region 染料

    def _on_current_dye_change(self, current: QModelIndex, previous: QModelIndex):
        """
        图片列表当前行变化事件
        :param current: 当前行索引
        :param previous:
        :return:
        """
        self.dye_index = current.row()
        cur_dye = self.dyes[self.dye_index]
        self.lineEditDyeName.setText(cur_dye.name)
        self.lineEditDyeNum.setText(str(cur_dye.value))

    def _load_dye(self):
        """
        加载染料和催化剂数据
        :return:
        """
        self.dye_model.clear()
        self.dye_model.setHorizontalHeaderLabels(['名称', '数量'])
        for dye in self.dyes:
            self.dye_model.appendRow([QStandardItem(dye.name), QStandardItem(str(dye.value))])

    def _add_dye(self):
        name = self.lineEditDyeName.text()
        num = self.lineEditDyeNum.text()
        if not name or not num:
            QMessageBox.information(self, '提示', '染料名称或数量不能为空！', QMessageBox.Ok)
            return
        self.dyes.append(FormulaItem(name=name, value=num))
        self.dye_model.appendRow([QStandardItem(name), QStandardItem(num)])
        self.tableViewDye.clearSelection()
        self.tableViewDye.selectRow(len(self.dyes) - 1)
        self.lineEditDyeName.clearFocus()
        self.lineEditDyeNum.clearFocus()

    def _update_dye(self):
        if not self._valid_dye_index():
            QMessageBox.information(self, '提示', '未选中染料！', QMessageBox.Ok)
            return
        name = self.lineEditDyeName.text()
        num = self.lineEditDyeNum.text()
        if not name or not num:
            QMessageBox.information(self, '提示', '染料名称或数量不能为空！', QMessageBox.Ok)
            return
        self.dyes[self.dye_index] = FormulaItem(name=name, value=float(num))
        self.dye_model.setItem(self.dye_index, 0, QStandardItem(name))
        self.dye_model.setItem(self.dye_index, 1, QStandardItem(num))
        self.lineEditDyeName.clearFocus()
        self.lineEditDyeNum.clearFocus()

    def _del_dye(self):
        if not self._valid_dye_index():
            QMessageBox.information(self, '提示', '未选中染料！', QMessageBox.Ok)
            return
        del self.dyes[self.dye_index]
        # self.tableViewDye.clearSelection()
        self.dye_model.removeRow(self.dye_index)
        self.lineEditDyeName.clear()
        self.lineEditDyeNum.clear()
        self.dye_index = -1
        self.tableViewDye.clearSelection()

    def _search_dye(self):
        name = self.lineEditDyeName.text()
        formula = self.formula_model.get_item(self.formula_index)
        dyes = formula.dyes
        if name:
            dyes = [x for x in dyes if name in x.name]
        num = self.lineEditDyeNum.text()
        if num:
            dyes = [x for x in dyes if num in x.value]
        self.dyes = dyes
        self.dye_index = -1
        self._load_dye()

    def _valid_dye_index(self):
        return 0 <= self.dye_index < len(self.dyes)

    # endregion

    # region 催化剂

    def _on_current_catalyzer_change(self, current: QModelIndex, previous: QModelIndex):
        """
        图片列表当前行变化事件
        :param current: 当前行索引
        :param previous:
        :return:
        """
        self.catalyzer_index = current.row()
        cur_catalyzer = self.catalyzers[self.catalyzer_index]
        self.lineEditCatalyzerName.setText(cur_catalyzer.name)
        self.lineEditCatalyzerNum.setText(str(cur_catalyzer.value))

    def _load_catalyzer(self):
        """
        加载催化剂和催化剂数据
        :return:
        """
        self.catalyzer_model.clear()
        self.catalyzer_model.setHorizontalHeaderLabels(['名称', '百分比'])
        for catalyzer in self.catalyzers:
            self.catalyzer_model.appendRow([QStandardItem(catalyzer.name), QStandardItem(f'{catalyzer.value}%')])

    def _add_catalyzer(self):
        name = self.lineEditCatalyzerName.text()
        num = self.lineEditCatalyzerNum.text()
        if not name or not num:
            QMessageBox.information(self, '提示', '催化剂名称或数量不能为空！', QMessageBox.Ok)
            return
        num = float(num)
        self.catalyzers.append(FormulaItem(name=name, value=float(num)))
        self.catalyzer_model.appendRow([QStandardItem(name), QStandardItem(f'{num}%')])
        self.tableViewCatalyzer.clearSelection()
        self.tableViewCatalyzer.selectRow(len(self.catalyzers) - 1)
        self.lineEditCatalyzerName.clearFocus()
        self.lineEditCatalyzerNum.clearFocus()

    def _update_catalyzer(self):
        if not self._valid_catalyzer_index():
            QMessageBox.information(self, '提示', '未选中催化剂！', QMessageBox.Ok)
            return
        name = self.lineEditCatalyzerName.text()
        num = self.lineEditCatalyzerNum.text()
        num = num.replace('%', '')
        if not name or not num:
            QMessageBox.information(self, '提示', '催化剂名称或数量不能为空！', QMessageBox.Ok)
            return
        self.catalyzers[self.catalyzer_index] = FormulaItem(name=name, value=num)
        self.catalyzer_model.setItem(self.catalyzer_index, 0, QStandardItem(name))
        self.catalyzer_model.setItem(self.catalyzer_index, 1, QStandardItem(f'{num}%'))
        self.lineEditCatalyzerName.clearFocus()
        self.lineEditCatalyzerNum.clearFocus()

    def _del_catalyzer(self):
        if not self._valid_catalyzer_index():
            QMessageBox.information(self, '提示', '未选中催化剂！', QMessageBox.Ok)
            return
        del self.catalyzers[self.catalyzer_index]
        # self.tableViewCatalyzer.clearSelection()
        self.catalyzer_model.removeRow(self.catalyzer_index)
        self.lineEditCatalyzerName.clear()
        self.lineEditCatalyzerNum.clear()
        self.catalyzer_index = -1
        self.tableViewCatalyzer.clearSelection()

    def _search_catalyzer(self):
        name = self.lineEditCatalyzerName.text()
        formula = self.formula_model.get_item(self.formula_index)
        catalyzers = formula.catalyzers
        if name:
            catalyzers = [x for x in catalyzers if name in x.name]
        num = self.lineEditCatalyzerNum.text()
        if num:
            catalyzers = [x for x in catalyzers if num in x.value]
        self.catalyzers = catalyzers
        self.catalyzer_index = -1
        self._load_catalyzer()

    def _valid_catalyzer_index(self):
        return 0 <= self.catalyzer_index < len(self.catalyzers)

    # endregion
