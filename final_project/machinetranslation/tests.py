'''These are test cases for translator.py'''

import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        self.assertEqual(english_to_french('omelette'),'Omelette')
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        self.assertEqual(english_to_french(None),'Input is null')
        self.assertEqual(french_to_english(None),'l entree est nulle')
if __name__ == "__main__":
    unittest.main()
