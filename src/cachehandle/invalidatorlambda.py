#!/usr/bin/env python

import boto3
import md5
import random
import datetime

def pathCtor( bucketkey ):
   return '/' + bucketkey

def md5Gen():
   string = str( datetime.datetime.now() ) + str( random.randint( 1, 1000 ) ) + 'bp'
   keygen = md5.new()
   keygen.update( string )
   return keygen.hexdigest()

def getBucketKey( event ):
   return event[ "Records"][ 0 ][ "s3" ][ "object" ][ "key" ]

def getBatch( path ):
   return {
         # Create some unique hash
         'CallerReference' : md5Gen(),
         'Paths' : {
            'Quantity' : 1,
            'Items' : [ path ]
         }
   }

def invalidator( event, context ):
   bucketkey = getBucketKey( event )
   path = pathCtor( bucketkey )
   cloudfront = boto3.client( 'cloudfront' )
   batch = getBatch( path )
   for dist in [ 'E2M4H8CW6MDHUR', 'E1JMZAU5DIWBYH' ]:
      cloudfront.create_invalidation( DistributionId=dist, InvalidateionBatch=batch )
