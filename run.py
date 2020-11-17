import pyperclip  #importing pyperclip for copying to clipboard
from password import User  #imporing user class
from credential import Credential #importing credential class

def create_user(fname, lname, password):
	'''
	Function to create a new user account
	'''
	new_user = User(fname, lname, password)
	return new_user


def save_user(user):
	'''
	Function to save a new user account
	'''
	User.save_user(user)


def verify_user(first_name, password):
	'''
	Function that verifies the existence of the user before creating credentials
	'''
	check_user = Credential.check_user(first_name, password)
	return check_user

def generate_password():
	'''
	Function to generate a password automatically
	'''
	password_gen = Credential.generate_password()
	return password_gen

def check_existing_credential(credential_account):
    '''
    Function that check if a credential exists with that credential_account and return a Boolean
    '''
    return Credential.find_by_credential_name(credential_account)

def add_credential(username, credential_account, account_name, password):
	'''
	Function to create a new credential
	'''
	new_credential = Credential(username, credential_account, account_name, password)
	return new_credential

def create_credential(username, credential_account, account_name, password):
	'''
	Function to create a new credential
	'''
	new_credential = Credential(username, credential_account, account_name, password)
	return new_credential

def save_credential(credential):
	'''
	Function to save a newly created credential
	'''
	Credential.save_credentials(credential)

def del_credential(credential_account):
    '''
    Function to delete a credential
    '''
    Credential.delete_credentials()

def display_credentials(username):
	'''
	Function to display saved credentials
	'''
	return Credential.display_credentials(username)

def find_credential(credential_account):
    '''
    Function that finds a contact by number and returns the contact
    '''
    return Credential.find_by_credential_name(credential_account)

def copy_credential(credential_account):
	'''
	Function to copy a credentials details to the clipboard
	'''
	return Credential.copy_credential(credential_account)

   










if __name__ == '__main__':
	main()