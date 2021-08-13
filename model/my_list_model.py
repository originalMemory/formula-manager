#!/user/bin/env python
# coding=utf-8
"""
@project : DeviceManager
@ide     : PyCharm
@file    : my_list_model
@author  : wuhoubo
@desc    : 自定义列表类，用于在列表展示数据
@create  : 2019/6/5 22:23:20
@update  :
"""
from abc import abstractmethod

from PyQt5.QtCore import QAbstractListModel, QModelIndex, QVariant, Qt


class MyListModel(QAbstractListModel):
    """
    Model类，用于listView展示
    """

    def __init__(self):
        super().__init__()
        self._data_list = []  # 数据list，保存所有数据

    def data(self, index: QModelIndex, role: int = ...):
        """
        继承父类，必须有。设置不同类型调用返回数据
        :param index: 索引
        :param role: 要获取的数据类型
        :return:
        """
        # 设置表格显示使用的数据
        if index.isValid() or (0 <= index.row() < len(self._data_list)):
            if role == Qt.DisplayRole:
                return QVariant(self._get_display_role(index.row()))
        else:
            return QVariant()

    @abstractmethod
    def _get_display_role(self, row):
        """
        根据索引获取对应位置显示的值
        :param row:
        :return:
        """
        pass

    def rowCount(self, parent: QModelIndex = ...) -> int:
        """
        继承父类，必须有。返回数据总行数
        :param parent:
        :return:
        """
        return len(self._data_list)

    def add_item(self, item_data):
        """
        自定义。添加单个数据
        :param item_data: 数据
        :return:
        """
        if item_data:
            self.beginInsertRows(QModelIndex(), len(self._data_list), len(self._data_list) + 1)
            self._data_list.append(item_data)
            self.endInsertRows()

    def add_items(self, item_data_list):
        """
        自定义。添加多个数据
        :param item_data_list: 数据列表
        :return:
        """
        if item_data_list:
            self.beginInsertRows(QModelIndex(), len(self._data_list), len(self._data_list) + len(item_data_list))
            self._data_list.extend(item_data_list)
            self.endInsertRows()

    def delete_item(self, row):
        """
        自定义。删除数据
        :param row: 索引
        :return:
        """
        self.beginRemoveRows(QModelIndex(), row, row - 1)
        item = self._data_list[row]
        del self._data_list[row]
        self.endRemoveRows()
        return item

    def update_item(self, row, new_item):
        """
        自定义。更新数据
        :param row: 索引
        :param new_item:
        :return:
        """
        self._data_list[row] = new_item
        index = self.index(row, 0)
        self.dataChanged.emit(index, index, [Qt.DisplayRole])

    def get_item(self, row):
        """
        自定义。获取数据
        :param row: 索引
        :return:
        """
        if -1 < row < len(self._data_list):
            return self._data_list[row]

    def clear(self):
        """
        清空数据
        :return:
        """
        self.beginResetModel()
        self._data_list.clear()
        self.endResetModel()
