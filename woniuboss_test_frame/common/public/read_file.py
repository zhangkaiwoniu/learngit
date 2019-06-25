#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
from woniuboss_test_frame.util.parse_excel import ParseExcel
from xml.etree import ElementTree


class ReadFile:
    """
    调用read_excel方法，读取excel文件，主要用于读取data数据
    调用read_xml方法，读取xml文件，主要用于读取配置信息
    """

    def read_excel(self,file_name):
        #读取excel调用方法，返回所有数据，以字典形式存储
        result = ParseExcel().return_all_data(file_name) #调用具体业务方法
        return result

    def read_xml(self,file_name,node_name):
        #读取xml文件，根据节点node_name返回内容，以列表形式返回
        datas = []
        tree = ElementTree.parse(file_name)
        root = tree.getroot()
        for i in root.iter(node_name):
            datas.append(i.text)
        return datas

if __name__ == '__main__':
    read = ReadFile()
    # sheet = read.read_xls("..\datas\data.xlsx")
    # data = read.parse_xls(sheet)
    # result = read.parse_datas(data)
    result = read.read_excel("..\..\data\data.xls")
    print(result)
    # node = read.read_xml(r"..\config\config.xml","host")
    # print(node)




