#!/usr/bin/env python

'''
This is a barebone server implementation
To be used by the backend EC2 servers
'''

from rdshandle import rdshandle
import BaseHTTPServer
import boto3
import os
import json

AWS_ACCESS_ID = os.environ.get( 'AWS_ACCESS_ID' )
AWS_SECRET_KEY = os.environ.get( 'AWS_SECRET_KEY' )
assert len( AWS_ACCESS_ID ) > 0, 'Please set AWS access key'
assert len( AWS_SECRET_KEY ) > 0, 'Please set AWS secret key'

WEBSERVER_PORT = 8000

class HTTPHandler( BaseHTTPServer.BaseHTTPRequestHandler ):
   '''
   handle requests based on the method
   '''
   def post( self ):
      ''' handles post request '''
      pass

   def do_GET( self ): #pylint: disable=invalid-name
      ''' handles get request '''
      def parseQueryString( path ):
         tokens = path.replace( '/?', '' ).split( '&' )
         return dict( [ t.split( '=' ) for t in tokens if '=' in t ] )

      self.send_response( 200 )
      self.send_header( 'Content-type', 'text/html' )
      self.end_headers()
      tokenized = parseQueryString( self.path )
      result = "Not processed"
      if 'action' in tokenized:
         rds = rdshandle.RDS()
         if tokenized[ 'action' ] == 'about':
            result = rds.fetch( tokenized[ 'username' ], rdshandle.User )
            result = result.__dict__ # TODO for now
         elif tokenized[ 'action' ] == 'list':
            resultList= rds.searchfiles( tokenized[ 'username' ] )
            result = [ result.__dict__ for result in resultList ]
         else:
            result = 'action not found'
      self.wfile.write( json.dumps( result ) )

def run_backend_server():
   '''
   run HTTP server listening to the port
   '''
   BaseHTTPServer.HTTPServer( ( '', WEBSERVER_PORT ), HTTPHandler ).serve_forever()

if __name__ == '__main__':
   run_backend_server()
