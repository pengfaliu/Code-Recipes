#coding: utf-8
import smtplib
from email.mime.multipart import MIMEMultipart#python2.4及之前版本该模块不是这样调用的，而是email.MIMEMultipart.MIMEMultipart(),下同
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
sender = 'monitor@163.com'#发件人地址
receiver = '123456789@qq.com'#收件人地址
smtpserver = 'smtp.qq.com'#邮件服务器
username = 'monitor'#用户名
password = 'xxxxx'#密码
smtp = smtplib.SMTP()

def send_email(msg,file_name):
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = file_name#邮件标题，这里我把标题设成了你所发的附件名
    msgText = MIMEText('%s'%msg,'html','utf-8')#你所发的文字信息将以html形式呈现
    msgRoot.attach(msgText)
    att = MIMEText(open('%s'%file_name, 'rb').read(), 'base64', 'utf-8')#添加附件
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="%s"'%file_name
    msgRoot.attach(att)
    while 1:#持续尝试发送，直到发送成功
        try:
            smtp.sendmail(sender, receiver, msgRoot.as_string())#发送邮件 
            break
        except:
            try:
                smtp.connect(smtpserver)#连接至邮件服务器
                smtp.login(username, password)#登录邮件服务器
            except:
                print "failed to login to smtp server"#登录失败

if __name__ == "__main__":
    MSG=""#要发送的文字
    FILE=""#要发送的文件
    send_email(MSG,FILE)
