import unittest
import pyperclip 
from password import User  
from credential import Credential 

class TestUser(unittest.TestCase):

    def setUp(self):
       
        self.new_user = User('Gisele', 'Tesire', '123456')

    def test_init(self):
       
        self.assertEqual(self.new_user.first_name,"Gisele")
        self.assertEqual(self.new_user.last_name,"Tesire")
        self.assertEqual(self.new_user.password,"123456")

    def test_save_user(self):
       
        self.new_user.save_user()
        self.assertEqual(len(User.users_list),1)
        
    def tearDown(self):
           
        User.users_list = []
               
class TestCredentials(unittest.TestCase):
    
    def setUp(self):
        
        self.new_credential = Credential('tesire','instagram','tesiregisele','123456')

    def test__init__(self):
        '''
		Test to check if the reation of credential instances is properly done
		'''
        self.assertEqual(self.new_credential.username,'tesire')
        self.assertEqual(self.new_credential.credential_account,'instagram')
        self.assertEqual(self.new_credential.account_name,'tesiregisele')
        self.assertEqual(self.new_credential.password,'123456')