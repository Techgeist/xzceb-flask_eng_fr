'''These are test cases for translator.py'''

import unittest
from translator import englishToFrench, frenchToEnglish

class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(englishToFrench('Hello'),'Bonjour')
        self.assertEqual(englishToFrench('omelette'),'Omelette')
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')
        self.assertEqual(englishToFrench(None),'Input is null')
        self.assertEqual(frenchToEnglish(None),'l entree est nulle')
if __name__ == "__main__":
    unittest.main()
