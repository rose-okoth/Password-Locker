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

    