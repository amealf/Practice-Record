# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 15:03:09 2020

@author: Great World
"""
import pandas as pd
import numpy as np
#from costatrade import Strategy
from matplotlib import pyplot as plt
from matplotlib.widgets import Cursor #十字光标
import matplotlib.ticker as ticker
import time
import os

def read_data(filename):  
    df = pd.read_excel(filename, names=['Time', 'Price', 'Direction', 'vol'])
    return df

df = read_data('temp data.xlsx')
df.index = pd.to_datetime(df['Time'],format = '%H:%M:%S')
df['amount'] = df['Price'].mul(df['vol'])
#print(df)

rule_cycle = '1S'  # rule_cycle='5T'：意思是5分鐘，意味着轉變爲5分鐘數據  # 15T  1H  1D 一天

cycle_df = df.resample('1S').sum()  # 初始化一個空的DataFrame，用戶接收新的數據.

print(cycle_df)