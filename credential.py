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