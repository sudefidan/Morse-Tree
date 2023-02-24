
from morse import MorseTree

if __name__ == "__main__":
    morse = MorseTree()
    e = morse.encode('us') 
    print('%s' % e)
    d = morse.decode(e)
    assert morse.encode('us') == '..- ...', "Should be ..-" 
    #assert morse.decode('..- ...') == 'us', "Should be ..-"