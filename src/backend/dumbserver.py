#!/usr/bin/env python

'''
This is a barebone server implementation
To be used by the backend EC2 servers
'''

from rdshandle import rdshandle
import BaseHTTPServer
import boto3
import os
import md5
import json
import cloudfront
import tempfile
import cgi

AWS_ACCESS_ID = os.environ.get( 'AWS_ACCESS_ID' )
AWS_SECRET_KEY = os.environ.get( 'AWS_SECRET_KEY' )
assert len( AWS_ACCESS_ID ) > 0, 'Please set AWS access key'
assert len( AWS_SECRET_KEY ) > 0, 'Please set AWS secret key'

WEBSERVER_PORT = 8000

def writeTempFile( content ):
   '''
   Writes a content to a temporary file and returns the path to it
   '''
   n = tempfile.NamedTemporaryFile( delete=False )
   n.write( content )
   n.close()
   return n.name

def toS3( filecontent, extension='' ):
   path = writeTempFile( filecontent )
   print path
   s3 = boto3.resource('s3',
                        aws_access_key_id=AWS_ACCESS_ID,
                        aws_secret_access_key=AWS_SECRET_KEY )
   try:
      binary = open( path, 'rb' )
      # Upload  the file to S3
      # Update RDS
      keygen = md5.new()
      keygen.update( filecontent )
      hashstring = keygen.hexdigest()
      print 'HASH is', hashstring
      hashstring += '.' + extension
      s3.Bucket( 'shinhw2b1' ).put_object( Key=hashstring, Body=binary )
   finally:
      os.remove( path )
   return hashstring

class HTTPHandler( BaseHTTPServer.BaseHTTPRequestHandler ):
   '''
   handle requests based on the method
   '''
   def do_POST( self ):
      ''' handles PUT request '''
      length = self.headers[ 'Content-Length' ]
      username = self.headers[ 'username' ]
      self.send_response( 200 )
      self.send_header( 'Content-type', 'text/html' )
      content = self.rfile.read( int( length ) )
      lines = content.split( '\n')

      # show some details to output
      print length
      print username

      # Some sanity check on file contente
      assert '----' in lines[0]
      assert 'Content-Disposition' in lines[1]
      assert 'name' in lines[1]
      assert 'filename' in lines[1]
      assert 'Content-Type' in lines[2]
      assert '----' in lines [-2]

      # extract the inner data
      filename = lines[1].split( '"' )[3]
      filecontent = '\n'.join( lines[4:-2] )

      # Add suffix to bucket key so that browser
      # can open it easily
      if '.' in filename:
         ext = filename.split( '.' )[-1]
      else:
         ext = ''

      # insert into S3 bucket
      bucketkey = toS3( filecontent, ext )

      # save into db
      rds = rdshandle.RDS()
      newFile = rdshandle.Object( '', filename, username, '',  bucketkey=bucketkey )
      print newFile.bucketkey(), 'is the new bucket key'
      rds.insert( ( newFile, ) )

      result = 'success'
      wrapper = { 'error' : '', 'result':  result }
      self.wfile.write( json.dumps( wrapper ) )

   def do_OPTIONS( self ):
      self.send_response( 200 )
      self.send_header( 'Access-Control-Allow-Origin', '*' )
      self.send_header( 'Access-Control-Allow-Methods', 'OPTIONS, POST, GET' )
      self.send_header( 'Access-Control-Allow-Headers', 'Content-type' )
      self.send_header( 'Access-Control-Allow-Headers', 'Content-length' )
      self.send_header( 'Access-Control-Allow-Headers', 'username' )
      self.end_headers()

   def do_GET( self ): #pylint: disable=invalid-name
      ''' handles get request '''
      def parseQueryString( path ):
         tokens = path.replace( '/?', '' ).split( '&' )
         return dict( [ t.split( '=' ) for t in tokens if '=' in t ] )

      self.send_response( 200 )
      self.send_header( 'Access-Control-Allow-Origin', '*' )
      self.send_header( 'Access-Control-Allow-Methods', 'OPTIONS, POST, GET' )
      self.send_header( 'Access-Control-Allow-Headers', 'Content-type' )
      self.send_header( 'Access-Control-Allow-Headers', 'Content-length' )
      self.send_header( 'Content-type', 'text/html' )
      self.end_headers()
      tokenized = parseQueryString( self.path )
      wrapper = { 'error' : 'invalid request', 'result': ''}
      if 'action' in tokenized:
         rds = rdshandle.RDS()
         if tokenized[ 'action' ] == 'about':
            result = rds.fetch( tokenized[ 'username' ], rdshandle.User )
            result = result.__dict__
            wrapper = { 'error': '', 'result': result }
         elif tokenized[ 'action' ] == 'list':
            resultList= rds.searchfiles( tokenized[ 'username' ] )
            result = [ result.__dict__ for result in resultList ]
            wrapper = { 'error': '', 'result': result }
         elif tokenized[ 'action' ] == 'fetchurl':
            identifier = tokenized[ 'id' ]
            fileObj = rds.fetch( identifier, rdshandle.Object )
            distUrl = '.'.join( cloudfront.getDistUrl().split('.')[:-1] )
            result = 'http://%s/%s' % ( distUrl, fileObj.bucketkey() )
            wrapper = { 'error': '', 'result' : result }
         else:
            wrapper = { 'error': 'action not found', 'result' : '' }
      print wrapper
      self.wfile.write( json.dumps( wrapper ) )

def run_backend_server():
   '''
   run HTTP server listening to the port
   '''
   BaseHTTPServer.HTTPServer( ( '', WEBSERVER_PORT ), HTTPHandler ).serve_forever()

if __name__ == '__main__':
   run_backend_server()
