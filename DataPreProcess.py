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
    pd.set_option('display.max_columns', None)     #在控制台显示所有列
    # print(df.head(10)) #打印前十行
    return df

def PreProcess(df):
    '''
    初步的数据预处理
    :parma df:已导入的DataFrame
    :return df:padas里的DataFrame对象
    '''
    df.drop(labels=['MobileEncrypt','IdCardNoEncrypt'],inplace=True,axis=1)   #删除手机号码和身份证号两列，原因：已脱敏，无用信息
    print(df.head(10))
    return df

if __name__=='__main__':
    df=LoadData('E:\中惠旅杯\DataSet\门票数据2021\门票数据.csv')
    PreProcess(df)
