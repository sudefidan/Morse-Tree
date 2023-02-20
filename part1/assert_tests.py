import morse
from morse import MorseTree

def test_encode_us():
    assert morse.encode('us') == '..- ...', "Should be ..- ..."

morse = MorseTree()
test_encode_us()