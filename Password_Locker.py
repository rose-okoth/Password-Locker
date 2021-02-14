#! /usr/bin/env python3
from users import User, Credentials
import pyperclip

    def new_user(username,password):
        '''
        Function for creating a new user
        '''
        new_user = User(username,password)
        return new_user

    def save_user(user):
        '''
        Function for new user account
        '''
        User.save_user(user)

    def verify_user(username,password)
        '''
        Function for user verification
        '''
        verifying_user = Credentials.check_user(username,password)
        return verifying_user

    def generate_password():
        '''
        Function for automatic passwords
        '''
        gen_pass = Credential.generate_password()
        return gen_pass

    def create_credential(name,site_name,password):
        '''
        Function for new credentials
        '''
        new_credential = Credential(name,site_name,password)
        return new_credential

    def save_credential(credential):
        '''
        Function to save a new credential
        '''
        Credential.save_credentials(credential)

    def display_credentials(name):
        '''
        Function for the credentials saved by the user
        '''
        return Credential.display_credentials(name)

    def copy_credential(site_name):
        '''
        Function for copying credentials to the clipboard
        '''
        return Credential.copy_credential(site_name)

    
    