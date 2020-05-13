
#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author : liufapeng
# date : 2019-12-17
    
import cherrypy
import urllib
import HtmlWritetoPDF

scans = []

class Scans:
    
  exposed = True
    
  def GET(self):
    return ('Here are all the scans: %s\n' % scans)
    
  def POST(self, content):
    # cherrypy.response.status = 404
    # cherrypy.response.headers['Custom-Title'] = urllib.parse.quote_plus('My custom error')
    # cherrypy.response.headers['Custom-Message'] = urllib.parse.quote_plus('The record already exists.')
            
    # in ms, if not set automatic time depending on the length, 0 = forever
    cherrypy.response.headers['qrinfo'] = '5000'
    
    scans.append(content)
    return ('Append new scan with content: %s' % content)
    
if __name__ == '__main__':
    
  conf = {
  'global': {
    'server.socket_host': '0.0.0.0',
    'server.socket_port': 8080
  },
  '/': {
    'request.dispatch': cherrypy.dispatch.MethodDispatcher()
  }
  }
    
  cherrypy.quickstart(Scans(), '/scans/', conf)
    
