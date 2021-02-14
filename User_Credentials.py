# Users and User Credentials

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
    credentials=[]
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

    def __init__(self,)