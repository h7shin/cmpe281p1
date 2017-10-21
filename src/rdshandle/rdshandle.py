#!/usr/bin/env python

import datetime
import MySQLdb

class Row( object ):
   '''
   Class about SQL row
   '''
   def insert( self ):
      ''' TODO For now just return SQL query '''
      query = 'INSERT INTO {table} ( {fields} ) VALUES ( {values} )'
      fields,values = self.keysvalues()
      return query.format( table=self.__class__.__name__,
                           fields=fields,
                           values=values )

   def keysvalues( self ):
      ''' Get lists of params and lists of values '''
      keys = []
      values = []
      for k, v in self.__dict__.iteritems():
         if k.endswith( '_' ):
            keys.append( k )
            values.append( '"' + v + '"' )
      return ',',join( keys ), ','.join( values )

   def update():
      ''' TODO will do this later '''

   def delete():
      ''' TODO For now just return SQL query '''
      query = 'DELETE FROM {table} WHERE {condition}'
      fields, values = self.keysValues()
      conditions = []
      for i in range( len( fields ) ):
         condition = '%s = "%s"' % ( fields[i], valyes[i] )
         conditions.append( condition )
      return query.format( table=self.__class__.__name__,
                           condition=" AND ".join( conditions ) )


class User( Row ):
   '''
   Class about user
   '''
   key = 'username'

   def __init__( self, username, firstname, lastname, email ):
      self.username_ = username
      self.firstname_ = firstname
      self.lastname_ = lastname
      self.email_ = email

   def username( self ):
      return self.username_

   def firtname( self ):
      return self.firstname_

   def email( self ):
      return self.email_

class Object( Row ):
   '''
   Class about file object
   '''
   key = 'id'
   groupby = 'username'

   def __init__( self, id, filename, username, description,
                 uploaded=datetime.datetime.now(),
                 updated=datetime.datetime.now() ):
      self.id_ = id
      self.filename_ = filename
      self.username_ = username
      self.description_ = description
      self.updated_ = updated
      self.uploaded_ = uploaded

   def id( self ):
      ''' returns object id '''
      return self.id_
   
   def filename( self ):
      return self.filename_

   def username( self ):
      return self.username_

   def description( self ):
      return self.desription_

   def updated( self ):
      return self.updated_

   def uploaded( self ):
      return self.uploaded_

   def setUpdated( self, time=datetime.datetime.now() ):
      self.updated_ = datetime.datetime.strftime( time, '%Y-%m-%d %H:%M:%S' )

   def setUploaded( self, time=datetime.datetime.now() ):
      self.uploaded_ = datetime.datetime.strftime( time, '%Y-%m-%d %H:%M:%S' )

class RDS( object ):
   def __init__( self ):
      user = 'root'
      passwd = raw_input( 'Enter password for this RDS instance:' )
      host = 'cmpe281p1db.cmqx6tpknayx.us-east-2.rds.amazonaws.com'
      db = 'cmpe281p1'
      self.conn = MySQLdb.connect( host=host, user=user, passwd=passwd, db=db )

   def record( self, identifier, classtype ):
      query = 'SELECT * FROM {table} WHERE {key} = "{identifier}"'
      cursor = self.conn.cursor()
      cursor.execute( query.format( table=classtype.__name__,
                      key=classtype.key,
                      identifier=identifier ) )
      return [ classtype( *row ) for row in cursor ]

   def searchfiles( self, username ):
      query = 'SELECT * FROM {table} WHERE {field} = "{identifier}"'
      cursor = self.conn.cursor()
      cursor.execute( query.format( table='Object',
                      field=Object.groupby,
                      identifier=username ) )
      return [ classtype( *row ) for row in cursor ]

if __name__ == '__main__':
   rds = RDS()
   print rds.record( '', Object )
   print rds.searchfiles( 'charles' )
