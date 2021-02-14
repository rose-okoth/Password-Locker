import unittest 
import pyperclip
from User_Credentials import User,Credentials

class TestUser(unittest.TestCase):

    '''
    Test for user class
    '''
    def setUp(self):
        self.new_user = User('Rose','rudim3nt@l')

    def test__init__(self):
        self.assertEqual(self.new_user.username,'Rose')
        self.assertEqual(self.new_user.password,'rudim3nt@l')

    def test_save(self):
        self.new_user.save_user()
        self.assertEqual(len(User.users),1)
    
class TestCredentials(unittest.TestCase):
    '''
    Test class for the credentials class
    '''


