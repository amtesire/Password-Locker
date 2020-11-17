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