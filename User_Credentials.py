# Users and User Credentials
import string
import pyperclip
import random

class User:
    '''
    Class for users to save their information
    '''
    users = []

    def __init__(self,username,password):
        '''
        Method for user properties
        '''
        self.username = username
        self.password = password

    def save_user(self):
        '''
        Function for saving new users
        '''
        User.users.append(self)

class Credentials:
    '''
    Class for user credentials
    '''
    credentials = []
    user_credentials = []

    @classmethod
    def check_user(cls,username,password):
        '''
        Method for verifying username and password
        '''
        current_user = ''
        for user in User.users:
            if (user.username == username and user.password == password):
                    current_user = username
        return current_user

    def __init__(self,name,site_name,password):
        '''
        Method for user objects
        '''
        self.name = name
        self.site_name = site_name
        self.password = password

    def generate_password(size = 10, char = string.ascii_uppercase + string.ascii_lowercase + string.digits):
        '''
        Method for new passwords
        '''
        gen_pass=''.join(random.choice(char) for _ in range(size))
        return gen_pass

    def save_credentials(self):
        '''
        Method for saving new user credentials
        '''
        Credentials.credentials.append(self)

    @classmethod
    def display_credentials(cls,name):
        '''
        Method for list of credentials
        '''
        user_credentials = []
        for credential in cls.credentials:
            user_credentials.append(credential)
        return user_credentials

    @classmethod
    def find_by_site_name(cls,site_name):
        '''
        Method returns a credential based on its site name
        '''
        for credential in cls.credentials:
            if credential.site_name == site_name:
                return credential

    @classmethod
    def copy_credential(cls,site_name):
        '''
        Method for copying credential info
        '''
        find_credential = Credentials.find_by_site_name(site_name)
        return pyperclip.copy(find_credential.password)