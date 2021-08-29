import requests
import json
from openpyxl import load_workbook  # 用于读取xlsx格式文件


def gain_location(adress):
    # 这个api_url网址里的city=填你想填的城市名（非必需参数，即可删除city=xxx），ak=填入你自己的密匙，output=json意思是输出json格式
    api_url = f'https://api.map.baidu.com/geocoding/v3/?address={adress}&ak=oKoFiY4qEUyiD4Uh6sj1uQA6pqFE1BQ2&output=json&callback=showLocation'

    r = requests.get(api_url)
    r = r.text

    '''经历以下两次去除，使得最终结果为json格式的数据 
       原来的数据格式：showLocation&&showLocation(' showLocation&&showLocation('showLocation&&showLocation({"status":0,"result":{"location":{"lng":108.94646555063274,"lat":34.34726881662395},"precise":0,"confidence":12,"comprehension":63,"level":"城市"}}）
       去除后的数据格式为将json字符串转换为字典类型：showLocation&&showLocation({"status":0,"result":{"location":{"lng":108.94646555063274,"lat":34.34726881662395},"precise":0,"confidence":12,"comprehension":63,"level":"城市"}}
    '''
    r = r.strip('showLocation&&showLocation(')
    r = r.strip(')')

    jsonData = json.loads(r)  # 将json字符串转换为字典类型转为字典格式类型

    return jsonData


# ******************************************读取xlsx文件,并使用百度接口函数将文件地名数据转为经纬度，并改成一定的格式*******************************************************

wb = load_workbook(filename="有用的地区数据.xlsx")  # 打开文件
ws = wb.get_sheet_by_name('Sheet1')  # 打开工作表，括号里输入要打开的工作表名字
rows = ws.rows  # 读取此工作表的所有行

for row in rows:  # 遍历工作表的每一行

    line = [col.value for col in row]  # line = 正在遍历的这一行，line是个列表，其中line[0]是地名，line[1]是地名计数

    if gain_location(line[0]).get('result', False):  # 因为有时候提取到的数据错误，所以要判断是否有result这个键，如果没有就跳过，继续下一个

        # 因为爬到几百个数据可能会出现长时间未响应自动结束的问题，所以加个异常处理
        try:
            lng = gain_location(line[0])['result']['location']['lng']  # 提取网址返回的经度
            lat = gain_location(line[0])['result']['location']['lat']  # 提取网址返回的纬度
            count = line[1]  # 地名计数

            str_temp = '{"lat":' + str(lat) + ',"lng":' + str(lng) + ',"count":' + str(count) + '},'  # 将经度，纬度，计数变成格式
            print(str_temp)  # 打印出格式，要待会儿直接要复制打印结果到别的文件中
        except:
            print(line[0])  # 打印出出问题的地名