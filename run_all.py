#!/usr/bin/python
# -*- coding:utf-8 -*-

import unittest
import smtplib
import os
import time
from common.HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


#获取当前运行的目录
dirpath = os.path.dirname(os.path.realpath(__file__))
print("当前运行的目录是：%s " %dirpath)

#获取用例目录用join拼接
casepath = os.path.join(dirpath,"test_case")

print("用例目录是：%s" %casepath)

#获取报告的目录
now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
reportpath=os.path.join(dirpath,'report', '%sreport.html' %now)
print("报告的目录是：%s" %reportpath)

#查找用例
all_cases=unittest.defaultTestLoader.discover(casepath,pattern='test*.py')
print(all_cases)

fp = open(reportpath,'wb')

runner = HTMLTestRunner(stream=fp,
                        title='自动化测试报告TEST',
                        description='自动化测试报告',
                        )

def TOemail():
    smtpserver='smtp.qq.com'
    port =465
    sender='741841851@qq.com'
    psw = 'tkxmercrmgnbbdgd'
    recevier = "741841851@qq.com"


    with open(reportpath,'rb') as f:
        mail_body=f.read().decode('utf-8')

    msg = MIMEMultipart()
    msg['from']=sender#发件人
    msg['to']=recevier#收件人
    msg['subject']='这是我的主题99'#主题

    # 正文
    body = MIMEText(mail_body,'html','utf-8')
    msg.attach(body)
    #附件
    att = MIMEText(mail_body,'base64','gbk')#用utf-8会出现乱码
    att['Content-Type']='application/octet-stream'
    att['Content-Disposition']='attachment;filename="test_report.html"'
    msg.attach(att)

    ####发送邮件
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)#连接服务器
        smtp.login(sender,psw)#登录
    except:
        smtp = smtplib.SMTP_SSL(smtpserver,port)
        smtp.login(sender,psw)#登录

    smtp.sendmail(sender,recevier,msg.as_string())#发送邮件
    smtp.quit()

runner.run(all_cases)
TOemail()


















