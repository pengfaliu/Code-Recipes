#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author : liufapeng
# date : 2019-12-18

import tornado
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options, parse_config_file
from tornado.web import Application, RequestHandler, url
import time
import __logger__


# 处理响应用户的请求
# url : 127.0.0.1:8080/

class IndexHandler(RequestHandler):
    
    log_file_name = 'qrserver.log'
    qrinfo_file_name = 'qrinfo.csv'
    today = time.strftime("%Y-%m-%d",time.localtime())
        
    def post(self,*args,**kwargs):
        post_data = self.get_body_argument('qrinfo')
        print('{}: {}'.format(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()),post_data))
        __logger__.get_logger(level='INFO')
        self.write('{}'.format("scan successful"))
        #return post_data

    #def 
if __name__ == "__main__":
    
    # 端口名为port，类型为整型，默认值为10000，不是一组值
    define('port', type=int, default=8080, multiple=False)
    
    # 从指定的配置文件中读取port,从当前文件的路径下寻找config文件
    #parse_config_file('config')    
    url_list = [('/scans/', IndexHandler)]

    app = Application(url_list)
    server = HTTPServer(app)
    server.listen(options.port)
    IOLoop.current().start()
    