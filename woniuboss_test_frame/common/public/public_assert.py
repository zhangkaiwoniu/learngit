#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
import traceback
from woniuboss_test_frame.common.public.output_log_screen import LogScreen

class Assert:
    """
    公共断言方法，调用方式：Assert.assert_method(type,hope,actual)
    type：断言方式：相等equal，包含in，大于greater，身份相等is,为none
    hope:期望结果
    actual:实际结果
    """

    @staticmethod
    def assert_method(testCase,type,hope,actual,dr=None):
        try:
            if type == "equal":
                testCase.assertEqual(hope,actual,"断言失败")
            elif type == "in":
                testCase.assertIn(hope,actual,"断言失败")
            elif type == "greater":
                testCase.assertGreater(hope,actual,"断言失败")
            elif type == "is":
                testCase.assertIs(hope,actual,"断言失败")
            elif type == "none":
                testCase.assertIsNone(actual,"断言失败")
            else:
                print("请输入正确断言类型")
        except Exception as e:
            LogScreen().excecut(traceback.format_exc(),dr)
            raise