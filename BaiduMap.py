import pandas as pd
import numpy as np
import json
from urllib.request import urlopen, quote
import requests

data = pd.read_csv('地区数据部分.csv',index_col=0)

def getlnglat(address):
    url = 'https://api.map.baidu.com/geocoding/v3/'
    output = 'json'
    ak = 'oKoFiY4qEUyiD4Uh6sj1uQA6pqFE1BQ2' # 百度地图ak，具体申请自行百度，提醒需要在“控制台”-“设置”-“启动服务”-“正逆地理编码”，启动
    address = quote(address) # 由于本文地址变量为中文，为防止乱码，先用quote进行编码
    uri = url + '?' + 'address=' + address  + '&output=' + output + '&ak=' + ak
    response=requests.get(uri)
    # req = urlopen(uri)
    # res = req.read().decode()
    temp = json.loads(response.text)
    lat = temp['result']['location']['lat']
    lng = temp['result']['location']['lng']
    return lat,lng   # 纬度 latitude   ，   经度 longitude  ，

#
# for indexs in data.index:
#     get_location = getlnglat(data.loc[indexs, '地区'])
#     get_lat = get_location[0]
#     get_lng = get_location[1]
#     data.loc[indexs, '纬度'] = get_lat
#     data.loc[indexs, '经度'] = get_lng
# data.to_csv('地区数据代码.csv')

#
data_left=pd.read_csv('地区数据全部.csv',index_col=0)
data_right=pd.read_csv('地区数据代码.csv',index_col=0)
# # data_all=pd.merge(data_left,data_right,how='left')
# # print(data_right)
# data_right.drop(labels=['Unnamed: 0'],inplace=True,axis=1)
# print(data_right)

# def getlnglat_1(address):
#     df=data_right.loc[data_right['地区']==address]
#     lat=df['经度'].iloc[0]
#     lng=df['纬度'].iloc[0]
#     # print(lat,lng)
#     return lat,lng
#
# for indexs in data_left.index:
#     get_location = getlnglat_1(data_left.loc[indexs, '地区'])
#     get_lat = get_location[0]
#     get_lng = get_location[1]
#     data_left.loc[indexs, '纬度'] = get_lat
#     data_left.loc[indexs, '经度'] = get_lng
# # print(data_left)


print(data_left.duplicated().sum())

# data_html = pd.DataFrame(columns=['content'])
# for indexs in data_right.index:
#     data_html.loc[indexs,'content'] = '{' + \
#                                       '"lat":' + str(data_right.loc[indexs,'纬度']) + ',' +  \
#                                       '"lng":' + str(data_right.loc[indexs,'经度']) + ','+'"count":1'  \
#                                       '}' + ','
#
# data_html.to_csv ("data_html1.csv",encoding="gbk")