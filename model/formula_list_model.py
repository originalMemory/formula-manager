# coding=utf-8
"""
@project : formula-manager
@ide     : PyCharm
@file    : formula_list_model
@author  : illusion
@desc    : 
@create  : 2021/8/11 1:58 下午:19
"""
from model.my_list_model import MyListModel


class FormulaListModel(MyListModel):
    def _get_display_role(self, row):
        return self._data_list[row].color_no
