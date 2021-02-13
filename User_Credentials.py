# Users and User Credentials

class User:
    '''
    Class for users to save their information
    '''
    users = []

    def _init_(self,username,password):
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
