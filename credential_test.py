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

    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credential object is saved into
         the credential list
        '''
        self.new_credential.save_credentials() # saving the new credential
        
        self.assertEqual(len(Credential.list_of_credentials),1)
        
    def test_save_multiple_credentials(self):
        '''
        test_save_multiple_credential to check if we can save multiple credentials
        objects to our list_of_credentials
        '''
        self.new_credential.save_credentials()
        test_credential = Credential("gizo","social","tesiregisele","112233") # new credential
        test_credential.save_credentials()
        
        self.assertEqual(len(Credential.list_of_credentials),2)

    def tearDown(self):
           
        Credential.list_of_credentials = []

    def test_find_by_credential_name(self):
        '''
		Test to check if we can find a credential by credential_account
		'''
        self.new_credential.save_credentials()
        test_user = Credential('gisele','github','amtesire','123456')
        test_user.save_credentials()
        
        credential_exists = Credential.find_by_credential_name('github')
        self.assertEqual(credential_exists,test_user)

    def test_display_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''
        self.new_credential.save_credentials()
        test_user = Credential('gisele','github','amtesire','123456')
        test_user.save_credentials()
        
        self.assertEqual(Credential.display_credentials(User),Credential.user_credentials_list)

    def test_copy_credential(self):
        '''
		Test to confirm if we can copy a credential from saved credentials
		'''
        self.new_credential.save_credentials()
        test_user = Credential('gisele','github','amtesire','123456')
        test_user.save_credentials() 
        Credential.copy_credential('123456')
        
        self.assertEqual(self.new_credential.password,pyperclip.paste())
        print(pyperclip.paste())
  
        
if __name__ == '__main__':
    unittest.main()