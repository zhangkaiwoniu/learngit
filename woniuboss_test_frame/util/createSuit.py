#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
import unittest
from woniuboss_test_frame.common.public.read_file import ReadFile
import os


class CreateSuit:

    @classmethod
    def create_suit(cls):
        type = ReadFile().read_xml(r".\config\config.xml", "type")  # 得到测试类型gui or interface
        suite = unittest.TestSuite()  # 创建测试套件
        discover = unittest.defaultTestLoader.discover(
            os.path.abspath(os.path.join("testcase", "%s_testcase" % type[0])) + "\\", pattern="test*.py",
            top_level_dir=None) #根据测试类型，动态载入testcase
        suite.addTests(discover) #添加testcase
        return suite

