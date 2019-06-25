#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
import unittest
from woniuboss_test_frame.common.public.public_login import PublicLogin

class TestDemo(unittest.TestCase):

    def test_demo(self):
        dr = PublicLogin().login("/WoniuBoss2.0")
        dr.quit()

