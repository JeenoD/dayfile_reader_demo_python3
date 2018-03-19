"""
# 用来存放股票每日数据类
# -*- coding: utf-8 -*-
# @Author : Jeeno
# @Time   : 2018/1/10 13:29
# @File   : Stock.py
"""

class Stock(object):
    def __init__(self):
        super(object).__init__()
        self.Date = ''
        self.OpenPrice = 0.0
        self.ClosePrice = 0.0
        self.HighPrice = 0.0
        self.LowPrice = 0.0
        self.Amount = 0
        self.Volume = 0

    def setStock(self, stockinfo):
        if stockinfo:
            self.Date = stockinfo[0]
            self.OpenPrice = stockinfo[1]/100
            self.HighPrice = stockinfo[2]/100
            self.LowPrice = stockinfo[3]/100
            self.ClosePrice = stockinfo[4]/100
            self.Amount = stockinfo[5]
            self.Volume = stockinfo[6]