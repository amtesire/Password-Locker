import pyperclip #importing pyperclip for copying to clipboard
from password import User #importing user class 
import random #import random variable generator
import string  #import string constants

class Credential:

	list_of_credentials =[]
	user_credentials_list = []

	def __init__(self,username,credential_account,account_name,password):
		
		self.username = username
		self.credential_account = credential_account = credential_account
		self.account_name = account_name
		self.password = password

    @classmethod
	def check_user(cls,first_name,password):
		
		current_user = ''
		for user in User.users_list:
			if (user.first_name == first_name and user.password == password):
				current_user = user.first_name
		return current_user


	def save_credentials(self):
		'''
		Function to save a newly created user credentials
		'''

		Credential.list_of_credentials.append(self)


	@classmethod
	def delete_credentials(self):
		'''
		Function to delete  credentials
		'''

		Credential.list_of_credentials.remove(self)

	def generate_password(size=8, char=string.ascii_lowercase+string.ascii_lowercase+string.digits):
		'''
		Function to generate a secure 8 character password for a user.
		'''
		password_gen=''.join(random.choice(char) for _ in range(size))
		return password_gen