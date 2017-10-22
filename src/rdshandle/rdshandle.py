#!/usr/bin/env python

import datetime
import MySQLdb
import os

class Row( object ):
   '''
   Class about SQL row
   '''
   def insert( self, conn ):
      ''' Insert this object into database '''
      query = 'INSERT INTO {table} ( {fields} ) VALUES ( {values} )'
      fields,values = self.keysvalues( False )
      cursor= conn.cursor()
      cursor.execute( query.format( table=self.__class__.__name__,
                                  fields=','.join( fields ),
                                  values=','.join( values ) ) )
      conn.commit()

   def keysvalues( self, skipKey=False ):
      ''' Get lists of params and lists of values '''
      keys = []
      values = []
      for k, v in self.__dict__.iteritems():
         if k.endswith( '_' ) and (
               not skipKey or k != self.__class__.key ):
            keys.append( ''.join( k.split( '_' )[:-1] ) )
            values.append( '"' + v + '"' )
      return keys, values

   def update( self, conn ):
      ''' Update this object in the database '''
      query = 'UPDATE {table} SET {newpairs} WHERE {key} = "{identifier}"'
      newpairs = []
      fields, values = self.keysvalues( True )
      for i in range( len( fields ) ):
         pair = '%s = %s' % ( fields[i], values[i] )
         newpairs.append( pair )
      cursor = conn.cursor()
      cursor.execute( query.format( table=self.__class__.__name__,
                           newpairs=" , ".join( newpairs ),
                           key=self.__class__.key,
                           identifier=self.identifier() ) )
      conn.commit()

   def delete( self, conn ):
      ''' Deletes this object from database '''
      query = 'DELETE FROM {table} WHERE {condition}'
      fields, values = self.keysvalues()
      conditions = []
      for i in range( len( fields ) ):
         condition = '%s = %s' % ( fields[i], values[i] )
         conditions.append( condition )
      cursor = conn.cursor()
      cursor.execute( query.format( table=self.__class__.__name__,
                           condition=" AND ".join( conditions ) ) )
      conn.commit()


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

   def identifier( self ):
      return self.username_

   def username( self ):
      return self.username_

   def firstname( self ):
      return self.firstname_

   def email( self ):
      return self.email_

   def lastnameIs( self, lastname ):
      self.lastname_ = lastname

   def firstnameIs( self, firstname ):
      self.firstname_ = firstname

   def emailIs( self, email ):
      self.email_ = email

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
      self.updated_ = datetime.datetime.strftime( uploaded, '%Y-%m-%d %H:%M:%S' )
      self.uploaded_ = datetime.datetime.strftime( updated, '%Y-%m-%d %H:%M:%S' )

   def identifier( self ):
      return self.id_

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

   def updatedIS( self, time=datetime.datetime.now() ):
      self.updated_ = datetime.datetime.strftime( time, '%Y-%m-%d %H:%M:%S' )

   def uploadedIs( self, time=datetime.datetime.now() ):
      self.uploaded_ = datetime.datetime.strftime( time, '%Y-%m-%d %H:%M:%S' )

   def filenameIs( self, filename ):
      self.filename_ = filename

   def descriptionIs( self, description ):
      self.description_ = description


class RDS( object ):
   def __init__( self ):
      user = 'root'
      passwd = os.getenv( 'RDS_PASSWORD' )
      host = 'cmpe281p1db.cmqx6tpknayx.us-east-2.rds.amazonaws.com'
      db = 'cmpe281p1'
      self.conn = MySQLdb.connect( host=host, user=user, passwd=passwd, db=db )

   def insert( self, entries ):
      ''' Insert the entries in to db '''
      for entry in entries:
         entry.insert( self.conn )

   def update( self, entries ):
      ''' Update entries in the db '''
      for entry in entries:
         entry.update( self.conn )

   def delete( self, entries ):
      ''' Delete entries in the db '''
      for entry in entries:
         entry.delete( self.conn )

   def fetch( self, identifier, classtype ):
      ''' Fetch new object with primary key as <identifier> '''
      query = 'SELECT * FROM {table} WHERE {key} = "{identifier}"'
      cursor = self.conn.cursor()
      cursor.execute( query.format( table=classtype.__name__,
                      key=classtype.key,
                      identifier=identifier ) )
      return [ classtype( *row ) for row in cursor ][0]

   def searchfiles( self, username ):
      query = 'SELECT * FROM {table} WHERE {field} = "{identifier}"'
      cursor = self.conn.cursor()
      cursor.execute( query.format( table='Object',
                      field=Object.groupby,
                      identifier=username ) )
      return [ Object( *row ) for row in cursor ]

if __name__ == '__main__':
   rds = RDS()
   user = rds.fetch( 'charles01', User )
   user.email = 'testuser@aaa.com'
   print rds.searchfiles( 'charles01' )
