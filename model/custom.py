#!/user/bin/env python3
# coding=utf-8
"""
@project : formula-manager
@ide     : PyCharm
@file    : custom
@author  : illusion
@desc    : 
@create  : 2021/8/14
"""
from dataclasses import dataclass


@dataclass
class Custom:
    custom_id: int
    name: str
    formula_ids: [int]

    @staticmethod
    def from_dict(di):
        formula_ids = [int(x) for x in di['formula_ids'].split(';') if x.isdigit()]
        return Custom(custom_id=di['id'], name=di['name'], formula_ids=formula_ids)
