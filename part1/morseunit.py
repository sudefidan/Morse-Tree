import unittest
from morse import MorseTree

class TestMorse(unittest.TestCase):
    #task3
    def test_encode(self):
        self.assertEqual( tree.encode('us'), '..- ...') #true
        self.assertEqual( tree.encode('Sude Fidan'), '... ..- -.. . / ..-. .. -.. .- -.') #true
        self.assertEqual(tree.encode('2023'), '..--- ----- ..--- ...--') #true
        self.assertEqual(tree.encode('2023 + 2017'), '..--- ----- ..--- ...-- / .-.-. / ..--- ----- .---- --...') #true
        self.assertEqual(tree.encode('FIDAN'), '..-. .. -.. .- -.') #true
        self.assertEqual(tree.encode('WE LOVE PC !'), '.-- . / .-.. --- ...- . / .--. -.-. / -.-.--') #true
        self.assertNotEqual( tree.encode('benedict'), '-... . -. . -..') #false - benedict: -... . -. . -.. .. -.-. -
        self.assertNotEqual( tree.encode('internet of the things'), '.. -. - . .-. -. . - / --- ..-. / - .... . / - .... .. -. --.') #false - internet of the things:.. -. - . .-. -. . - / --- ..-. / - .... . / - .... .. -. --. ...
        
    def test_decode(self):
        self.assertEqual( tree.decode('...- ... -.-. --- -.. .'), 'VSCODE') #true
        self.assertEqual( tree.decode('... ..-.'), 'SF') #true
        self.assertEqual( tree.decode('- .... . / . -. -..'), 'THE END') #true
        self.assertEqual( tree.decode('..--- ----- ..--- ...-- / -....- / ..--- ----- ..--- ....-'), '2023 - 2024') #true
        self.assertNotEqual( tree.decode('.. -. - . .-. -.'), 'INTERNET') #false - INTERNET: .. -. - . .-. -. . -
        self.assertNotEqual( tree.decode('- .... .. -. --. .'), '2002') #false - 2002: ..--- ----- ----- ..---
        
    def test_is_empty(self):
        self.assertFalse(tree.is_empty()) #true

    def test_is_not_empty(self):
        self.assertTrue(tree.is_not_empty()) #true

    def test_find(self):
        self.assertIn(tree.find('.-'), tree.dict) #true

    def test_insert(self):
        tree.insert('.--.-.','@') 
        self.assertEqual(tree.find('.--.-.'), '@') #true
        self.assertIn(tree.find('.--.-.'),tree.dict) #true
        self.assertNotIn(tree.find('.........'),tree.dict) #true - doesn't exist in dictionary

    #task4
    def test_symbols(self):
        #TODO ADD SOME OTHER CHALLEGING TESTINGS
        self.assertEqual(tree.find('.-.-.-'), '.') #true
        self.assertEqual(tree.find('-.--.'), '(') #true
        self.assertEqual(tree.find('.-.-.'), '+') #true
        self.assertEqual(tree.find('..-.-'), '¿') #true
        self.assertEqual(tree.find('--..--'), ',') #true
        self.assertEqual(tree.find('-.--.-'), ')') #true
        self.assertEqual(tree.find('-....-'), '-') #true
        self.assertEqual(tree.find('--...-'), '¡') #true
        self.assertEqual(tree.find('..--..'), '?') #true
        self.assertEqual(tree.find('.-...'), '&') #true
        self.assertEqual(tree.find('..--.-'), '_') #true 
        self.assertEqual(tree.find('.----.'), '’') #true 
        self.assertEqual(tree.find('---...'), ':') #true 
        self.assertEqual(tree.find('.-..-.'), '”') #true 
        self.assertEqual(tree.find('-.-.--'), '!') #true 
        self.assertEqual(tree.find('-.-.-.'), ';') #true
        self.assertIn(tree.decode('-.-.-.'), tree.dict) #true - -.-.-.==> ; so it exist in morse dictionary
        self.assertNotEqual(tree.find('-.-.-.'), 'A') #false - -.-.-. ==> ;

if __name__ == '__main__':
    print('\n\n\n----------------------------- UNIT TESTING ---------------------------\n')
    tree = MorseTree()
    unittest.main()