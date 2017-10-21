#!/usr/bin/env python


'''
This is a barebone server implementation
To be used by the bacckend EC2 servers
'''

import BaseHTTPServer

WEBSERVER_PORT = 8000

class HTTPHandler(BaseHTTPServer.BaseHTTPRequestHandler):
   '''
   handle requests based on the method
   '''
   def post(self):
      ''' handles post request '''
      pass

   def do_GET(self): #pylint: disable=invalid-name
      ''' handles get request '''
      self.send_response(200)

def run_backend_server():
   '''
   run HTTP server listening to the port
   '''
   BaseHTTPServer.HTTPServer(('', WEBSERVER_PORT), HTTPHandler).serve_forever()

if __name__ == '__main__':
   run_backend_server()
