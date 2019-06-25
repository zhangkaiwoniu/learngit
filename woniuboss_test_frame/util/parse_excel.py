#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
import xlrd
from xml.etree import ElementTree


class ParseExcel:

    def get_sheet(self,file_name):
        data = xlrd.open_workbook(file_name)  # 通过路径找到excel
        sheet = data.sheet_by_index(0)  # 找到所需sheet
        return sheet

    def parse_xls(self,sheet):
        result = []
        other_all_data = []
        for i in range(1, sheet.nrows):
            other_data = []
            result.append(sheet.row_values(i)[4]) #得到所有的参数，放到result
            other_data.append(sheet.row_values(i)[2]) #得到url
            other_data.append(sheet.row_values(i)[3]) #得到请求类型
            other_data.append(sheet.row_values(i)[6]) #得到期望值
            other_data.append(sheet.row_values(i)[7]) #得到断言方式==或in
            other_all_data.append(other_data) #得到其他数据，放到other_all_data
        return result,other_all_data

    def parse_datas(self,datas,other_all_data):
        result = []
        for i in range(len(datas)):
            list = datas[i].split('\n')
            dicts = {} #其他数据存储字典
            dict = {} #参数数据存储字典
            for j in list:
                # dicts = {}  # 其他数据存储字典
                # dict = {}  # 参数数据存储字典
                if "=" in j:
                    key_value = j.split("=") #以=分隔
                    dict[key_value[0]] = key_value[1] #暂时存到dict中
            #将数据已字典形式存到dicts
            dicts["url"] = other_all_data[i][0]
            dicts["type"] = other_all_data[i][1]
            dicts["data"] = dict
            dicts["expectation"] = other_all_data[i][2]
            dicts["assert"] = other_all_data[i][3]
            #已列表形式存储虽有字典
            result.append(dicts)
        return result

    def return_all_data(self,file_name):
        #读取excel调用方法，返回所有数据，以字典形式存储
        sheet = self.get_sheet(file_name)
        datas,other_all_data = self.parse_xls(sheet)
        result = self.parse_datas(datas,other_all_data)
        return result