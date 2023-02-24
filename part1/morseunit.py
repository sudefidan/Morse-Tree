import unittest
from morse import MorseTree

class TestMorse(unittest.TestCase):
    def setUp(self):
        self.morse = MorseTree()

    #task3
    def test_encode(self):
        self.assertEqual( self.morse.encode('us'), '..- ...') #true
        self.assertEqual( self.morse.encode('sude'), '... ..- -.. .') #true
        self.assertEqual(self.morse.encode('iot'), '.. --- -') #true
        self.assertNotEqual(self.morse.encode('fidan'), '..-. .. ... .- -.') #false
        self.assertNotEqual( self.morse.encode('benedict'), '-... . -. . -..') #false
        
    def test_decode(self):
        self.assertEqual( self.morse.decode('...- ... -.-. --- -.. .'), 'VSCODE') #true
        self.assertEqual( self.morse.decode('... ..-.'), 'SF') #true
        self.assertEqual( self.morse.decode('- .... .'), 'THE') #true
        self.assertNotEqual( self.morse.decode('.. -. - . .-. -.'), 'INTERNET') #false
        self.assertNotEqual( self.morse.decode('- .... .. -. --. .'), 'THINGS') #false
        
    def test_is_empty(self):
        self.assertFalse(self.morse.is_empty()) #true

    def test_is_not_empty(self):
        self.assertTrue(self.morse.is_not_empty()) #true

    def test_find(self):
        self.assertIn(self.morse.find('.-'), 'A') #true

    def test_insert(self):
        self.morse.insert('.--.-.','@') 
        self.assertEqual(self.morse.find('.--.-.'), '@') #true
        self.assertIn(self.morse.find('.--.-.'),self.morse.dict) #true
        self.assertNotIn(self.morse.find('.........'),self.morse.dict) #true - doesn't exist in dictionary

    #task4
    def test_symbols(self):
        self.assertEqual(self.morse.find('.-.-.-'), '.') #true
        self.assertEqual(self.morse.find('-.--.'), '(') #true
        self.assertEqual(self.morse.find('.-.-.'), '+') #true
        self.assertEqual(self.morse.find('..-.-'), '¿') #true
        self.assertEqual(self.morse.find('--..--'), ',') #true
        self.assertEqual(self.morse.find('-.--.-'), ')') #true
        self.assertEqual(self.morse.find('-....-'), '-') #true
        self.assertEqual(self.morse.find('--...-'), '¡') #true
        self.assertEqual(self.morse.find('..--..'), '?') #true
        self.assertEqual(self.morse.find('.-...'), '&') #true
        self.assertEqual(self.morse.find('..--.-'), '_') #true 
        self.assertEqual(self.morse.find('.----.'), '’') #true 
        self.assertEqual(self.morse.find('---...'), ':') #true 
        self.assertEqual(self.morse.find('.-..-.'), '”') #true 
        self.assertEqual(self.morse.find('-.-.--'), '!') #true 
        self.assertEqual(self.morse.find('-.-.-.'), ';') #true 
        self.assertEqual(self.morse.find('...-..-'), '$') #true 

if __name__ == '__main__':
    unittest.main()