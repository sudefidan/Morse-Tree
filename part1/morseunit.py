import unittest
import morse

class TestMorse(unittest.TestCase): 
    def test_encode_us():
        self.assertEqual( morse.encode('us'), '..- ...')

if __name__ == '__main__': 
    unittest.main()