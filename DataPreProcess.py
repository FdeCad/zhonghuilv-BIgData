from typing import Mapping
import pandas as pd
import numpy as np


def LoadData(path):
    '''
    导入选定路径的数据集
    :parma path:选取路径
    :return df:padas里的DataFrame对象
    '''
    df=pd.read_csv(path,encoding='utf-8',error_bad_lines=False)
    print(df.head(10)) #打印前十行
    return df

if __name__=='__main__':
    df=LoadData('E:\中惠旅杯\大数据挑战赛数据集21-7-4\门票数据2021\门票数据.csv')

