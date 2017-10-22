#!/usr/bin/env python

import unittest
import invalidatorlambda

class InvalidatorTest( unittest.TestCase ):
   '''
   Unittest for Invalidator Lambda
   '''
   def testmd5( self ):
      ''' Make sure that md5Gen returns very unique string '''
      a = []
      for i in range( 100000 ):
         a.append( invalidatorlambda.md5Gen() )
      aset = set(a)
      assert len( aset ) == len( a )

   def testPathCtor( self ):
      ''' Very simple but still good to cover '''
      key = 'abc123'
      assert invalidatorlambda.pathCtor( key ) == '/' + key

   def testBucket( self ):
      event = { 'Records' : [{
                 's3' : {
                    'object' : {
                       'key' : 'bucketkey!'
                       }
                    }
                 }]
               }
      assert invalidatorlambda.getBucketKey( event ) == 'bucketkey!'

   def testBatch( self ):
      batch = invalidatorlambda.getBatch( 'a' )
      assert batch[ 'Paths' ][ 'Items' ][ 0 ] == 'a'

if __name__ == '__main__':
   unittest.main()
