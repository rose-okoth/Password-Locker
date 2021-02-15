#! /usr/bin/env python3
from User_Credentials import User, Credentials
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

def verify_user(username,password):
    '''
    Function for user verification
    '''
    verifying_user = Credentials.check_user(username,password)
    return verifying_user

def generate_password():
    '''
    Function for automatic passwords
    '''
    gen_pass = Credentials.generate_password()
    return gen_pass

def create_credential(name,site_name,password):
    '''
    Function for new credentials
    '''
    new_credential = Credentials(name,site_name,password)
    return new_credential

def save_credential(credential):
    '''
    Function to save a new credential
    '''
    Credentials.save_credentials(credential)

def display_credentials(name):
    '''
    Function for the credentials saved by the user
    '''
    return Credentials.display_credentials(name)

def copy_credential(site_name):
    '''
    Function for copying credentials to the clipboard
    '''
    return Credentials.copy_credential(site_name)




def main():
	print(' ')
	print('Hello! Welcome to Password Locker.')
	while True:
		print(' ')
		print("-"*20)
		print('Use these codes to navigate: \n nu-New User \n li-Log In \n ex-Exit')
		short_code = input('Enter a choice: ').lower().strip()
		if short_code == 'ex':
			break

		elif short_code == 'nu':
			print("-"*20)
			print(' ')
			print('To create a new account:')
			username = input('Enter your username - ').strip()
			password = input('Enter your password - ').strip()
			save_user(new_user(username,password))
			print(" ")
			print(f'New Account Created for: {username} using password: {password}')

		elif short_code == 'li':
			print("-"*20)
			print(' ')
			print('To login, enter your account details: ')
			username = input('Enter your username - ').strip()
			password = str(input('Enter your password - '))
			user_exists = verify_user(username,password)

			if user_exists == username:
				print(" ")
				print(f'Welcome {username}. Please choose an option to continue.')
				print(' ')

				while True:
					print("-"*20)
					print('Navigation codes: \n cc-Create a Credential \n dc-Display Credentials \n copy-Copy Password \n ex-Exit')
					short_code = input('Enter a choice: ').lower().strip()
					print("-"*20)

					if short_code == 'ex':
						print(" ")
						print(f'Goodbye, {username}')
						break

					elif short_code == 'cc':
						print(' ')
						print('Enter your credential details: ')
						name = input('Enter the name- ').strip()
						site_name = input('Enter the site\'s name- ').strip()
						# account_name = input('Enter your account\'s name - ').strip()

						while True:
							print(' ')
							print("-"*20)
							print('Please choose an option for entering a password: \n ep-enter existing password \n gp-generate a password \n ex-exit')
							psw_choice = input('Enter an option: ').lower().strip()
							print("-"*20)

							if psw_choice == 'ep':
								print(" ")
								password = input('Enter your password: ').strip()
								break

							elif psw_choice == 'gp':
								password = generate_password()
								break

							elif psw_choice == 'ex':
								break

							else:
								print('Oops! Wrong option entered. Try again.')
						save_credential(create_credential(name,site_name,password))
						print(' ')
						print(f'Credential Created: Site Name: {site_name} - Password: {password}')
						print(' ')

					elif short_code == 'dc':
						print(' ')

						if display_credentials(name):
							print('Here is a list of all your credentials')
							print(' ')
							for credential in display_credentials(name):
								print(f'Site Name: {credential.site_name} - Password: {credential.password}')
							print(' ')	

						else:
							print(' ')
							print("You don't seem to have any credentials saved yet")
							print(' ')

					elif short_code == 'copy':
						print(' ')
						chosen_site = input('Enter the site name for the credential password to copy: ')
						copy_credential(chosen_site)
						print('')

					else:
						print('Oops! Wrong option entered. Try again.')

			else: 
				print(' ')
				print('Oops! Wrong details entered. Try again or Create an Account.')		
		
		else:
			print("-"*20)
			print(' ')
			print('Oops! Wrong option entered. Try again.')
				
if __name__ == '__main__':
	main()