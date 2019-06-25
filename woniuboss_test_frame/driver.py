#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
import unittest
from woniuboss_test_frame.util.HTMLTestRunner import HTMLTestReportCN
import time
from woniuboss_test_frame.util.createSuit import CreateSuit
from woniuboss_test_frame.common.public.read_file import ReadFile
from woniuboss_test_frame.util.send_email import SendEmain
import os

class RunAllTest:
    """
    run方法入口方法，执行所需用例
    """
    config_path = os.path.abspath(".\config\config.xml") #获取配置文件路径

    def run(self):
        suite = CreateSuit.create_suit() #生成测试套件
        file = ".\\report.\\%sreport.html"%time.strftime("%Y%m%d%H%M%S",time.localtime(time.time())) #report报告打开路径
        with open(file,'wb') as f:
            #生成HTMLTestReport的runner对象
            runner = HTMLTestReportCN(
                stream=f, #报告路径
                verbosity=2, #输出内容的详细程度，1、2、3级
                title="测试报告" #标题
            )
            print("########开始执行测试##########")
            while True:
                start_time = time.strftime('%H_%M', time.localtime(time.time()))
                timing = ReadFile().read_xml(self.config_path, "time")[0]
                # 可设置一个定时器
                # if start_time == timing:
                if 1 == 1:
                    print('开始运行脚本：')
                    # 执行测试用例，通过HTMLTestReportCN类下的run方法执行套件中的用例方法，并生成测试报告
                    runner.run(suite)
                    # 执行发邮件
                    SendEmain().sendreport()
                    print("脚本运行完成!")
                    break
                else:
                    time.sleep(5)
                    print(start_time)

if __name__ == '__main__':
    RunAllTest().run()
    # print(os.getcwd())

