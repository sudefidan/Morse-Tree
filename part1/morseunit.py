import unittest
import morse
from morse import MorseTree

class TestMorse(unittest.TestCase):
    def setUp(self):
        self.morse = MorseTree()

    #task3
    def test_encode(self):
        unittest.TestCase.assertEqual( self,self.morse.encode('us'), '..- ...') #true
        unittest.TestCase.assertEqual( self,self.morse.encode('sude'), '... ..- -.. .') #true
        unittest.TestCase.assertNotEqual(self,self.morse.encode('fidan'), '..-. .. ... .- -.') #false
        unittest.TestCase.assertNotEqual( self,self.morse.encode('benedict'), '-... . -. . -..') #false
        unittest.TestCase.assertEqual( self,self.morse.encode('iot'), '.. --- -') #true

    def test_decode(self):
        unittest.TestCase.assertNotEqual( self,self.morse.decode('.. -. - . .-. -.'), 'INTERNET') #false
        unittest.TestCase.assertEqual( self,self.morse.decode('... ..-.'), 'SF') #true
        unittest.TestCase.assertEqual( self,self.morse.decode('- .... .'), 'THE') #true
        unittest.TestCase.assertNotEqual( self,self.morse.decode('- .... .. -. --. .'), 'THINGS') #false
        unittest.TestCase.assertEqual( self,self.morse.decode('...- ... -.-. --- -.. .'), 'VSCODE') #true

    def test_is_empty(self):
        #self.assertTrue(self.morse.is_empty()) #false
        self.assertFalse(self.morse.is_empty()) #true

    def test_is_not_empty(self):
        self.assertTrue(self.morse.is_not_empty()) #true
        #self.assertFalse(self.morse.is_not_empty()) #false 

    def test_find(self):
        self.assertEqual(self.morse.find('.-'), 'A') #true
        #self.assertIsNone(self.morse.find('..-.')) #false-does not exist

    def test_insert(self):
        self.morse.insert('.--.-.','@')
        self.assertEqual(self.morse.find('.--.-.'), '@') #true
        self.assertIn(self.morse.find('.--.-.'),self.morse.dict)
        
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