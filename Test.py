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
    def test_check_user(self):
        '''
        Function to verify whether the function check_user works
        '''
        self.new_user = User('Rose','rudim3nt@l')
        self.new_user.save_user()
        user2 = User('Rio','3liz@b3th')
        user2.save_user()

        for user in User.users:
            if user.username == user2.username and user.password == user2.password:
                current_user = user.username
        return current_user

        self.assertEqual(current_user,Credential.check_user(user2.password,user2.username))
    
    def setUp(self):
        '''
        Function for creating account creds before test
        '''
        self.new_credential = Credential('Rose','Instagram','inst@')

    def test__init__(self):
        '''
        Test to check on new credentials
        '''
        self.assertEqual(self.new_credential.name,'Rose')
        self.assertEqual(self.new_credential.site_name,'Instagram')
        self.assertEqual(self.new_credential.password,'inst@')
    
    def test_save_credentials(self):
        '''
        Test for credential info
        '''
        self.new_credential.save_credentials()
		instagram = Credential('Rose','Instagram','inst@')
		instagram.save_credentials()
		self.assertEqual(len(Credential.credentials),2)

