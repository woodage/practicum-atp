from unittest import *    
import doctest
import io
from contextlib import redirect_stdout

def isValidationCorrect(username, password):
	validUsername = "Admin"
	validPassword = "Geheim"
	
	if username == validUsername and password == validPassword:
		return True
	elif username == validUsername and password != validPassword:
		return False
	elif username != validUsername and password == validPassword:
		return False
	elif username != validUsername and password != validPassword:
		return False
	
	return False

class isValidationCorrectTest(TestCase):
    
    def test_is_validation_correct(self):
        self.assertTrue(isValidationCorrect("Admin", "Geheim"))
        self.assertFalse(isValidationCorrect("Admin", "geheim"))
        self.assertFalse(isValidationCorrect("admin", "Geheim"))
        self.assertFalse(isValidationCorrect("admin", "geheim"))

hwt = isValidationCorrectTest()                        # een simpelere manier van aanroepen is unittest.main() 
suite = TestLoader().loadTestsFromModule(hwt) # in plaats van deze drie regels, maar helaas werkt dat 
TextTestRunner().run(suite)                   # niet in IPython