#!/usr/bin/env python

import dns.resolver

DIST_CNAME = 'dist1.hyunwookshin.com'

def getDistUrl():
   return str( dns.resolver.query( DIST_CNAME, 'CNAME')[0].target )

