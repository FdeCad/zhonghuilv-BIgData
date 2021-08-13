'''
文件解释：此文件是一个爬虫
爬取结果：爬取百度百科的2019年12月中华人民共和国县以上行政区划代码
对于项目的作用：身份证信息虽已脱敏，但前六位任然可以查询身份证所有者所在地区，用于门票数据的数据预处理
@author：廖政荣
@time：2021-8-12
'''

import requests
from bs4 import BeautifulSoup

def GetUrl(url):
    response=requests.get(url)       #无反爬，直接get
    # print(response.status_code)      #打印返回状态码
    return response  #返回响应内容

def ParseResponse(response):
    soup=BeautifulSoup(response.text,'lxml')
    td=soup.find_all('td')
    dic={}     #定义空字典
    a=0        #计数器
    while(a<len(td)):
        dic[td[a].get_text()]=td[a+1].get_text()
        a=a+2   #两个一组，所以＋2
    return dic   #返回值，字典类型

# url='http://www.mca.gov.cn/article/sj/xzqh/1980/2019/202002281436.html'  #爬取网址
'''
#直接运行
res=GetUrl(url)           
ParseResponse(res)
'''