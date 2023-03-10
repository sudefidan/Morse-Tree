#SUDE FIDAN - 21068639

from morse import MorseTree

if __name__ == "__main__":
    morse = MorseTree()

    #task2
    e = morse.encode('us') 
    print('%s' % e)
    d = morse.decode(e)
    assert morse.encode('us') == '..- ...', "Should be ..-" 
    #assert morse.decode('..- ...') == 'us', "Should be ..-"
    
    #messages
    print('--------TEXT TO MORSE-------------')
    text_message = input(('Enter text to encode ==> '))
    encoded = morse.encode(text_message)
    print('Encoded message: ' + encoded)

    print('--------MORSE TO TEXT-------------')
    morse_message = input(('Enter morse to decode ==> '))
    decoded = morse.decode(morse_message)
    print('Decoded message: ' + decoded)

    #printing morse tree
    morse.print_tree(morse.root)