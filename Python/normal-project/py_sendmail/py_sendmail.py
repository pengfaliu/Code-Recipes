#!/usr/bin/python 
# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------------
# Name:        py_sendmail.py
# Purpose:     send mail by python scripts,.
# Author:      liufapeng
# Email:       pengfaliu@163.com
# Created:     19/10/2015  d/m/y
# Copyright:   (c) liufapeng 2015
# requirement: python >=2.4
# verion : 1.0.0
# Licence:     GPL V2
#-------------------------------------------------------------------------------
#system module
import sys
#sys.path.append("./python-ntlm-master")
reload(sys)
sys.setdefaultencoding('utf8')

#.ini module
import  ConfigParser

#mysql driver
import MySQLdb as mdb

#email
from email.mime.text import MIMEText 
from email.header import Header
from smtplib import SMTPException, SMTPAuthenticationError ,SMTP,SMTP_SSL

class opdb:
    def __init__(self,login_configfile,charset='utf8'):
        self.charset = charset
        self.configparser = ConfigParser.RawConfigParser()
        self.configparser.readfp(open(login_configfile))
        self.loginfo=dict(self.configparser.items('database')) 
              
      
    ##connect mysql
    def connect(self,*sqls):
        db = mdb.connect(host=self.loginfo['host'],port=self.loginfo['port'],user=self.loginfo['user'],passwd=self.loginfo['password'],db=self.loginfo['database'],charset=self.charset)
        cur = db.cursor()
        for sql in sqls:
            cur.execute(sql)
            db.commit()
        db.close()

    def query(self,*sqls): #only use  query
        db = mdb.connect(host=self.loginfo['host'],port=self.loginfo['port'],user=self.loginfo['user'],passwd=self.loginfo['password'],db=self.loginfo['database'],charset=self.charset)
        cur = db.cursor()
        for sql in sqls:
            cur.execute(sql)
            results = cur.fetchall()
            return results
        db.close()
        

########################################################################
class py_sendmail:
    """使用python 发送邮件的客户端类"""

    #----------------------------------------------------------------------
    def __init__(self,login_configfile,send_info_configfile):
        """Constructor"""
        self.configparser = ConfigParser.RawConfigParser()
        self.configparser.readfp(open(login_configfile))
        self.loginfo=dict(self.configparser.items('sender'))
    
    #def get_department(self,department):
        
    #def send_mail(self,to_list,subject,content): 
    def send_mail(self,department):
        """"""
        self.configparser.readfp(open(send_info_configfile))
        send_info=dict(self.configparser.items(department))
        
        sender = self.loginfo['nickname']+"<"+self.loginfo['mail_user']+self.loginfo['mail_postfix']+">" 
        msg = MIMEText(content) 
        msg['Subject'] = subject 
        msg['From'] = sender 
        msg['to'] = to_list 

        try: 
            s = SMTP() 
            s.set_debuglevel(1)
            s.connect(mail_host,587)
            #s.ehlo()
            s.starttls()
            s.ehlo()
        
            #ntlm_authenticate(s, mail_user, mail_pass)
            s.login(mail_user,mail_pass) 
            s.sendmail(me,to_list,msg.as_string()) 
            s.close() 
            return True 
        except Exception,e: 
            print str(e) 
            return False       
        



if __name__ == "__main__": 
    #send_mail(sys.argv[1], sys.argv[2], sys.argv[3]) 
    send_mail('pengfaliu@163.com', 'test', 'testtest')
