#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
from woniuboss_test_frame.common.public.read_file import ReadFile
from selenium import webdriver
import os

class Browers:

    @classmethod
    def choiceBrowers(cls):
        browers = ReadFile().read_xml(".\config\config.xml", "browser")[0] #读取配置文件信息，获取浏览器类型
        #根据浏览器类型，打开响应的浏览器，1--火狐，2--谷歌，3--IE
        if browers == "1":
            # driver_path = os.path.join(os.path.abspath("."), r"browers_driver\geckodriver.exe")
            dr = webdriver.Firefox()
        elif browers == "2":
            # driver_path = os.path.join(os.path.abspath("."), r"browers_driver\chromedriver.exe")
            dr = webdriver.Chrome()
        elif browers == "3":
            # driver_path = os.path.join(os.path.abspath("."), r"browers_driver\IEDriverServer.exe")
            dr = webdriver.Ie()
        else:
            dr = webdriver.Firefox()
        return dr
