#!/usr/bin/env python
#-- coding:utf-8 --

import sys
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import check_status

sys.path.insert(0,os.path.dirname(os.getcwd()))

url = check_status.url()

mail_host = 'smtp.xxx.com'
mail_user = 'user@xxx'
mail_pass = 'xxx'

#收件人
receivers = ['user1@xxx','user2@xxx']

#邮件内容
message = MIMEText('URL检测失败 :\n%s'%url,'plain','utf-8')
#对应邮件的显示标题
message['From'] = Header("xx告警",'utf-8')
#对应邮件标题的收件人
message['To'] = Header('user组','utf-8')

#邮件标题
subject = '邮件告警'
message['subject'] = Header(subject,'utf-8')

smtpobj = smtplib.SMTP('smtp.xxx.com')
smtpobj.login(mail_user,mail_pass)
smtpobj.sendmail(mail_user,receivers,message.as_string())
