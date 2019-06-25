#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
import unittest
import os, time, datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from woniuboss_test_frame.common.public.read_file import ReadFile

class SendEmain:
    config_path = os.path.abspath(".\config\config.xml")
    config_mail_from = ReadFile().read_xml(config_path, "mail_from")[0]
    config_mail_to = ReadFile().read_xml(config_path, "mail_to")[0]
    authorize = ReadFile().read_xml(config_path, "authorize")[0]
    # 发送邮件
    def sendmail(self,file_new):
        try:
            # 发信邮箱
            mail_from = self.config_mail_from
            # 收信邮箱
            mail_to = self.config_mail_to
            # 定义正文
            with open(file_new,'rb') as f:
                mail_body = f.read()
            # 生成一个邮箱客户端
            msg = MIMEMultipart()
            # 定义标题
            msg['Subject'] = "蜗牛进销存测试报告"
            msg['From'] = mail_from
            msg['To'] = mail_to
            # 定义发送时间（不定义的话，可能有的邮件客户端会不显示发送时间）
            msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
            # 得到正文，report.html中内容，类型是html，字符集utf-8
            textpart = MIMEText(mail_body, _subtype='html', _charset='utf8')
            #粘贴正文到客户端正文中
            msg.attach(textpart)
            # 邮件附件
            # htmlpart = MIMEApplication(open(file_new, 'rb').read())
            # htmlpart = MIMEApplication(mail_body)
            with open(file_new,'rb') as f:
                htmlpart =MIMEApplication(f.read())
            # htmlpart.add_header('Content-Disposition', 'attachment', filename=file_new.split('\\')[4])
            htmlpart.add_header('Content-Disposition', 'attachment', filename=file_new.split('\\')[2])
            #上传report.html文件附件到邮箱
            msg.attach(htmlpart)
            #smtp简单邮件传输协议
            smtp = smtplib.SMTP_SSL('smtp.qq.com', 465)
            #用授权码登陆邮箱
            smtp.login(self.config_mail_from, self.authorize)  # 授权码，非邮箱密码
            smtp.sendmail(mail_from, mail_to.split(','), msg.as_string())
            smtp.quit()
            print('邮件发送成功!')
        except smtplib.SMTPException as e:
            print('邮件发送失败!%s' % e)

    # 查到测试报告并发送邮件
    def sendreport(self):
        try:
            # result_dir = 'D:\\autotest\\web_auto_test_youyin\\report'
            lists = os.listdir('.\\report') #找到该目录下所有文件，已数组方式存储
            #将lists中文件按照日期排序，lambda中表达式为三元表达式，os.path.isdir()判断是文件夹还是文件
            #是文件的话为false，not false== true，为true执行os.path.getmtime()得到文件时间，传给key，根据内部算法排序
            lists.sort(key = lambda fn: os.path.getmtime('.\\report' + "\\" + fn) if not os.path.isdir('.\\report' + "\\" + fn) else 0)
            # 找到最新生成的文件
            file_new = os.path.join('.\\report', lists[-1])
            # 调用发邮件模块
            self.sendmail(file_new)
        except Exception as e:
            print(e)




