# coding=utf-8
"""
@project : formula-manager
@ide     : PyCharm
@file    : formula
@author  : illusion
@desc    : 
@create  : 2021/8/11 10:55 上午:30
"""
from dataclasses import dataclass


@dataclass
class FormulaItem:
    name: str
    value: float

    def to_str(self):
        return f'{self.name};{self.value}'

    @staticmethod
    def from_str(string):
        tup = string.split(';')
        if not len(tup):
            return None
        return FormulaItem(name=tup[0], value=float(tup[1]))


@dataclass
class Formula:
    formula_id: int
    color_no: str
    color_name: str
    quality: str
    dyes: [FormulaItem]
    catalyzers: [FormulaItem]

    @staticmethod
    def from_dict(di):
        dyes = [FormulaItem.from_str(x) for x in di['dyes'].split('\n') if x]
        catalyzers = [FormulaItem.from_str(x) for x in di['catalyzers'].split('\n') if x]
        return Formula(formula_id=di['id'], color_no=di['color_no'], color_name=di['color_name'], quality=di['quality'],
                       dyes=dyes, catalyzers=catalyzers)
