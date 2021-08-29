from typing import Mapping
import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False   #用来正常显示负号

def LoadData(path):
    '''
    导入选定路径的数据集
    :parma path:选取路径
    :return df:padas里的DataFrame对象
    '''
    df=pd.read_csv(path,encoding='utf-8',error_bad_lines=False)
    pd.set_option('display.max_columns', None)     #在控制台显示所有列
    pd.set_option('display.max_rows',None)
    # print(df.head(10)) #打印前十行
    return df
#
def ExchangeIdCity(df):
    with open('地区代码.json','r',encoding='utf-8') as f:   #打开地区代码
        cont=f.read()
        cdic=json.loads(cont)   #读取为字典
        # print(cdic)
    df['IdCardNoEncrypt']=df['IdCardNoEncrypt'].str.slice(0,6)
    #使用map替换地区代码
    # cdic['省直辖行政单位']
    df['IdCardNoEncrypt'] = df['IdCardNoEncrypt'].map(cdic)
    df['IdCardCity'].fillna(df['IdCardNoEncrypt'],inplace=True)
    return df


def PreProcess(df):
    '''
    初步的数据预处理
    :parma df:已导入的DataFrame
    :return df:padas里的DataFrame对象
    '''
    # df.drop(labels=['MobileServiceProvider','SettlementDate','MobileCity','IdCardProvince','MobileEncrypt','IdCardName','ThirdOrderNo','TeamOrderName','Sex','IdCardCity','MobileProvince','IdCardNoEncrypt'],inplace=True,axis=1)   #删除无用信息
    df.dropna(axis=0,inplace=True,how='any')  #删除空值行
    # print(df.duplicated().sum())
    df.drop_duplicates()  #去除重复数据
    df.index = range(df.shape[0])     #索引重构
    # df=ExchangeIdCity(df)
    # print(df.head(100))
    # print(df.isnull().sum())    #统计总体缺失值
    #对PersonNum进行数据类型转换
    df['PersonNum']=df['PersonNum'].astype('int')
    # print(df[(df.PersonNum>1000)])
    # print(df.describe())
    # print(df.info())
    # df1=df.iloc[0:5000,:]
    # df1.to_csv('test.csv',encoding='utf-8')
    return df

def DrawXiang(df):
    plt.figure()
    p=df.boxplot(return_type='dict')
    print(p)
    x=p['fliers'][0].get_xdata()
    y=p['fliers'][0].get_ydata()
    y.sort()
    for i in range(len(x)):
        if i > 0:
            plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.05 - 0.8 / (y[i] - y[i - 1]), y[i]))
        else:
            plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.08, y[i]))
    plt.show()


def GetPersonAdress(df):
    adr=pd.DataFrame()
    adr['地区']=df['IdCardProvince']+df['IdCardCity']
    # adr.dropna(axis=0,inplace=True,how='any')  #删除空值行
    adr['经度']=np.nan
    adr['纬度']=np.nan
    adr1=adr.drop_duplicates(subset='地区')  #去除重复数据
    adr.index = range(adr.shape[0])     #索引重构
    adr.to_csv('地区数据全部.csv',encoding='utf-8')
    adr1.to_csv('地区数据部分.csv',encoding='utf-8')

    print(adr.head(5000))

if __name__=='__main__':
    df=LoadData('E:\中惠旅杯\DataSet\门票数据2021\门票数据.csv')
    df1=PreProcess(df)
    # DrawXiang(df1['PersonNum'])
    GetPersonAdress(df)