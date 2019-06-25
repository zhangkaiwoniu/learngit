#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
import traceback
from woniuboss_test_frame.common.public.read_file import ReadFile
from woniuboss_test_frame.common.public.output_log_screen import LogScreen
from woniuboss_test_frame.util.choice_browers import Browers
import requests
import os


class PublicLogin():
    """
    正确填写配置信息，登陆只需调用login方法，此方法为类方法，调用方式PublicLogin.login(),
    注意PublicLogin后面不加括号
    """
    config_path = os.path.abspath(".\config\config.xml")
    #输出配置文件参数
    type = ReadFile().read_xml(config_path,"type")[0] #测试类型
    username = ReadFile().read_xml(config_path,"username")[0]
    password = ReadFile().read_xml(config_path,"password")[0]
    verifycode = ReadFile().read_xml(config_path,"verifycode")[0]
    host = ReadFile().read_xml(config_path,"host")[0] #主机名
    port = ReadFile().read_xml(config_path,"port")[0] #端口

    @classmethod
    def gui_login(cls,uri):
        #gui测试登陆，根据配置信息选择浏览器
        dr = Browers.choiceBrowers()
        #selenium登陆
        dr.set_page_load_timeout(30)
        dr.implicitly_wait(15)
        dr.maximize_window()
        dr.get(cls.host + cls.port + uri)
        uname = dr.find_element_by_xpath("//input[@name='userName']")
        uname.clear()
        uname.click()
        uname.send_keys(cls.username)
        pwd = dr.find_element_by_xpath("//input[@name='userPass']")
        pwd.clear()
        pwd.click()
        pwd.send_keys(cls.password)
        vcode = dr.find_element_by_xpath("//input[@name='checkcode']")
        vcode.clear()
        vcode.click()
        vcode.send_keys(cls.verifycode)
        dr.find_element_by_xpath("//button[@onclick='login();']").click()
        #进行断言，成功登陆返回drivr
        try:
            dr.find_element_by_link_text("注销")
            return dr
        except Exception as e:
            LogScreen().excecut(traceback.format_exc(),dr)
            dr.quit()
            raise

    @classmethod
    def interface_login(cls,uri):
        #接口测试登陆
        session = requests.session()
        #请求参数
        data = {
            'userName': cls.username,
            'userPass': cls.password,
            'checkcode': cls.verifycode
        }
        url = cls.host + cls.port + uri #接口地址
        try:
            resp = session.get(url=url, params=data) #发送请求
            # print(resp.text)
            assert (resp.text == "success") #进行断言，成功登陆返回session
            return session
        except Exception as e:
            LogScreen().excecut(traceback.format_exc())
            raise

    @classmethod
    def login(cls,uri):
        result = None
        #根据配置文件选择调用gui登陆还是interface登陆
        if cls.type == "gui":
            result = cls.gui_login(uri)
        elif cls.type == "interface":
            result = cls.interface_login(uri)
        else:
            print("请检查配置文件是否是否正确")
        return result


if __name__ == '__main__':
    data = ReadFile().read_excel("..\..\data\data.xls")
    print(data)
    # PublicLogin.login("/WoniuBoss2.0")
    # PublicLogin.login("/WoniuBoss2.0/log/userLogin")
    # print(PublicLogin.browers)
