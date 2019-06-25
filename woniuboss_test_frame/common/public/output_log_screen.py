#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
from time import strftime,localtime
import os
from woniuboss_test_frame.common.public.read_file import ReadFile

class LogScreen:
    """
    获取日志，如果是GUI测试，并且获取截图
    """
    config_path = os.path.abspath(".\config\config.xml") #获取配置文件地址

    def excecut(self,exp,drive = None):
        date_log = strftime("%Y%m%d",localtime()) #日志的时间
        date_screeen = strftime("%Y%m%d%H%M%S", localtime())  # 截图日期
        project_path = ReadFile().read_xml(self.config_path,"path")[0] #获取项目路径
        with open(os.path.join(project_path,"log\%slog.txt"%date_log),"a") as f: #打开日志文件
            time = "\n时间:" + date_screeen + "\n"
            f.write(time + exp) #写入日志
        if drive is not None : #如果是GUI测试，获取截图
            drive.get_screenshot_as_file(os.path.join(project_path,"screen\%serror.png"%date_screeen)) #截图并保存

# l = os.path.abspath("..\..\config\config.xml")
# print(l)