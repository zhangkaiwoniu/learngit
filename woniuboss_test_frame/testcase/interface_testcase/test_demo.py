#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
import unittest
import os
from woniuboss_test_frame.common.public.public_login import PublicLogin
from woniuboss_test_frame.common.public.read_file import ReadFile
from woniuboss_test_frame.common.public.public_assert import Assert
from ddt import ddt,data,unpack

@ddt
class TestDemo(unittest.TestCase):
    """
    unittest + ddt 框架
    """
    file_path = ".\data\data1.xls"
    config_path = os.path.abspath(".\config\config.xml")
    datas = ReadFile().read_excel(file_path) #得到所有数据，以每一行数据为一个字典，存在列表中
    host = ReadFile().read_xml(config_path, "host")[0]  # 主机名
    port = ReadFile().read_xml(config_path, "port")[0]  # 端口

    @classmethod
    def setUpClass(cls):
        cls.session = PublicLogin().login("/WoniuBoss2.0/log/userLogin")

    @data(*datas) #遍历datas列表,每次得到一个data，其是一个字典，可通过key得到value
    def test_demo(self,data):
        """
        此处给出编写方式，建议将以下代码编入各自的业务方法中，
        此处应该只用调用业务方法，得到响应，进行断言
        """
        uri = data["url"] #得到uri
        url = self.host + self.port + uri #拼接出接口地址
        param = data["data"] #得到接口请求参数
        request_type = data["type"] #得到请求类型
        hope = data["expectation"] #得到期望值
        assert_type = data["assert"] #得到断言类型
        resp = self.session.request(request_type,url=url,params=param) #发出请求，得到响应
        test_case = unittest.TestCase()
        Assert.assert_method(test_case,assert_type,hope,resp.text) #断言




