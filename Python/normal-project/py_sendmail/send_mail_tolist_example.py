#!/usr/bin/env python
#-*- coding: utf-8 -*-
#encoding = utf-8

#使用Python smtplib发送带附件的邮件给多人的时候
#样例程序

import smtplib, mimetypes
import time
from email.mime.text import MIMEText  
from email.mime.multipart import MIMEMultipart  
from email.mime.image import MIMEImage  

msg            = MIMEMultipart()  
msg['From']    = "mail1@163.com"
#msg['To']     = ["mail1@163.com","mail1@163.com","mail1@163.com"] 会出错
mail_to        = ["mail1@163.com","mail1@163.com","mail1@163.com"]
msg['To']      = ', '.join(mail_to)
msg['Subject'] = "Report " + (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

txt = MIMEText("User List \n\n\n")  
msg.attach(txt)
fileName = r'user_list.txt'  
ctype, encoding = mimetypes.guess_type(fileName)  
if ctype is None or encoding is not None:  
    ctype = 'application/octet-stream'  
maintype, subtype = ctype.split('/', 1)  
att1 = MIMEImage((lambda f: (f.read(), f.close()))(open(fileName, 'rb'))[0], _subtype = subtype)  
att1.add_header('Content-Disposition', 'attachment', filename = fileName)  
msg.attach(att1)  
smtp = smtplib.SMTP()  
smtp.connect('smtp.139.com:25')  
smtp.login('user', 'password')  
#smtp.sendmail(msg['From'], msg['To'], msg.as_string()) 会出错  
smtp.sendmail(msg['From'], mail_to, msg.as_string())  
smtp.quit()  