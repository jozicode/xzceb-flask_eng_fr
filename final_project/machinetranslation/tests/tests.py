import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour") #test when Hello is given as input the output must be Bonjour.
        self.assertNotEqual(english_to_french("Hello"), "Hello") #test when Hello is given as input the output must be Bonjour, not Hello.

class TestFrenchToFrench(unittest.TestCase):
    def test(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello") #test when Bonjour is given as input the output must be Hello.
        self.assertNotEqual(french_to_english("Bonjour"), "Bonjour") #test when Bonjour is given as input the output must be Hello, not Bonjour. 

unittest.main()
