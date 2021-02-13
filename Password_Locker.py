from users import User
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

    
