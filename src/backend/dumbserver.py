#!/usr/bin/env/python

'''
This is a barebone server implementation
To be used by the bacckend EC2 servers
'''

WEBSERVER_PORT = 8000

class HTTPHandler(object):
   '''
   handle requests based on the method
   '''
   def post(self):
      ''' handles post request '''
      pass

   def get(self):
      ''' handles get request '''
      pass

def run_backend_server():
   '''
   run HTTP server listening to the port
   '''
   pass

if __name__ == '__main__':
   run_backend_server()
