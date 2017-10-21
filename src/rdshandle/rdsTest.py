#!/usr/bin/python

from rdshandle import User, Object, RDS
import unittest

class TestRdsHandle( unittest.TestCase ):
   '''
   TestRdsHandle tests the functionality of MySQL/RDS facing
   python script
   '''
   def setUp( self ):
      self.rds = RDS()

   def testUser( self ):
      bob = User( 'bobby', 'Bob', 'Smith', 'bobby@test.test' )
      tom = User( 'tommy', 'Tomas', 'Yong', 'tomasyong@test.test' )
      self.rds.insert( ( bob, tom ) )

      newbob = self.rds.fetch( 'bobby', User )
      newtom = self.rds.fetch( 'tommy', User )

      # Swap emails
      bobsemail = newbob.email()
      newbob.emailIs( newtom.email() )
      newtom.emailIs( bobsemail )

      # Update the entries
      self.rds.update( ( newbob, newtom ) )

      # Ensure that two entries are swapped
      assert self.rds.fetch( 'bobby', User ).email() == tom.email()
      assert self.rds.fetch( 'tommy', User ).email() == bob.email()

      # Delete two entries
      self.rds.delete( ( newbob, newtom ) )

   def testFile( self ):
      bob = User( 'bobby', 'Bob', 'Smith', 'bobby@test.test' )
      self.rds.insert( ( bob, ) )

      flower = Object( '01', 'flower.png', 'bobby', 'Picture of a flower' ) 
      note = Object( '02', 'note.txt', 'bobby', 'Some important notes' )
      self.rds.insert( ( flower, note ) )

      assert self.rds.fetch( '01', Object ).filename() == 'flower.png'
      assert self.rds.fetch( '02', Object ).filename() == 'note.txt'

      assert len( self.rds.searchfiles( 'bobby' ) ) == 2
      self.rds.delete( ( flower, note ) )
      assert len( self.rds.searchfiles( 'bobby' ) ) == 0

      self.rds.delete( ( bob, ) )

if __name__ == '__main__':
   unittest.main()
