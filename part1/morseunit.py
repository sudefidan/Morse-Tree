import unittest
from morse import MorseTree

class TestMorse(unittest.TestCase):
    #task3
    def test_encode(self):
        self.assertIn( tree.encode('here'), '.. / .- -- / .... . .-. . ') #true - here: .... . .-. .
        self.assertEqual( tree.encode('Sude Fidan'), '... ..- -.. . / ..-. .. -.. .- -.') #true
        self.assertCountEqual( '..--- ----- ..--- ...--', tree.encode('2023')) #true
        self.assertEqual(tree.encode('2023 + 2017'), '..--- ----- ..--- ...-- / .-.-. / ..--- ----- .---- --...') #true
        self.assertEqual(tree.encode('FIDAN'), '..-. .. -.. .- -.') #true
        self.assertEqual(tree.encode('WE LOVE PC !'), '.-- . / .-.. --- ...- . / .--. -.-. / -.-.--') #true
        self.assertNotEqual( tree.encode('benedict'), '-... . -. . -..') #false - benedict: -... . -. . -.. .. -.-. -
        self.assertNotEqual( tree.encode('internet of the things'), '.. -. - . .-. -. . - / --- ..-. / - .... . / - .... .. -. --.') #false - internet of the things:.. -. - . .-. -. . - / --- ..-. / - .... . / - .... .. -. --. ...
        self.assertNotIn(tree.encode('s'), tree.dict)

    def test_decode(self):
        self.assertIn(tree.decode('... ..-.'), 'SF IS MY CAPITALS') #true -  SF: ... ..-.
        self.assertEqual( tree.decode('...- ... -.-. --- -.. .'), 'VSCODE') #true
        self.assertCountEqual('THE END',tree.decode('- .... . / . -. -..')) #true
        self.assertEqual( tree.decode('..--- ----- ..--- ...-- / -....- / ..--- ----- ..--- ....-'), '2023 - 2024') #true
        self.assertNotEqual( tree.decode('.. -. - . .-. -.'), 'INTERNET') #false - INTERNET: .. -. - . .-. -. . -
        self.assertNotIn( tree.decode('- .... .. -. --. .'), 'I WAS BORN IN 2002 ') #false - 2002: ..--- ----- ----- ..---

    def test_is_empty(self):
        self.assertFalse(tree.is_empty()) #true

    def test_is_not_empty(self):
        self.assertTrue(tree.is_not_empty()) #true

    def test_find(self):
        self.assertIn(tree.find('.-'), tree.dict) #true
        self.assertIn(tree.find('...'), 'SUDE') #true

    def test_insert(self):
        self.assertNotIn('@', tree.dict) #false - '@' hasn't implemented yet
        tree.insert('.--.-.','@') 
        self.assertEqual(tree.find('.--.-.'), '@') #true
        self.assertIn(tree.find('.--.-.'),tree.dict) #true - '@' has been implemented succesfully
        self.assertNotIn(tree.find('.........'),tree.dict) #true - doesn't exist in dictionary

    #task4
    def test_symbols(self):
        self.assertEqual(tree.find('.-.-.-'), '.') #true
        self.assertEqual(tree.find('..--.-'), '_') #true 
        self.assertIs(tree.decode('-....-'), '-') #true 
        self.assertIs(tree.find('--...-'), '¡') #true
        self.assertEqual(tree.decode('..--.. -.-.--'), '?!') #true ..--.. ==> ? AND -.-.-- ==> !
        self.assertEqual(tree.decode('-.--. / -.--.-'), '( )') #true -.--. ==> ( AND-.--.- ==> )
        self.assertIn(tree.find('...-..-'), '$€£') #true  ...-..- ==> $
        self.assertIn(tree.find('.----.'), '’') #true  .----. ==> ’
        self.assertIn(tree.decode('---...'), tree.dict) #true ---... ==> :
        self.assertIn('+', tree.dict) #true
        self.assertCountEqual('&',tree.find('.-...')) #true
        self.assertCountEqual(tree.encode('-'),'-....-') #true
        self.assertNotIn('¿¿¿', tree.dict) #true only one ¿ exist
        self.assertNotEqual(tree.find('-.-.-.'), 'A') #false - -.-.-. ==> ;
        self.assertNotEqual(tree.decode('.-..-'), '”') #false .-..-. ==> ”
        self.assertIsNot(',',tree.find('..--.-')) #false - , ==> --..--


if __name__ == '__main__':
    print('\n\n\n----------------------------- UNIT TESTING ---------------------------\n')
    tree = MorseTree()
    unittest.main()