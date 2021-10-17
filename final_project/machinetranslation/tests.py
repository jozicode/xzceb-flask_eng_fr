import unittest
from translator import englishToFrench
class TestenglishTofrench(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(englishToFrench('Hello'),'Bonjour')
        self.assertEqual(englishToFrench(0), 0)

from translator import frenchToEnglish
class TestfrenchToEnglish(unittest.TestCase):
    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')
        self.assertEqual(frenchToEnglish(0), 0)

if __name__=='__main__':
         unittest.main()
