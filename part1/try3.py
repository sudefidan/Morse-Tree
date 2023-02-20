class Node:
        def __init__(self,value=None):
            self.value = value
            self.left = None
            self.right = None
class MorseCode:

    MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
                       'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
                       'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
                       'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----',
                       '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
                       '9': '----.', ' ': '/'}
    
    def __init__(self):
        self.root = Node()
        for letter, code in self.MORSE_CODE_DICT.items():
            self.insert(code, letter, self.root)


    def insert(self, code, letter, node):
        for symbol in code:
            if symbol == '.':
                if node.left is None:
                    node.left = Node()
                node = node.left
            elif symbol == '-':
                if node.right is None:
                    node.right = Node()
                node = node.right
        node.value = letter

    def encode(self, text):
        encoded_text = ''
        for char in text.upper():
            if char in self.MORSE_CODE_DICT:
                code = self.MORSE_CODE_DICT[char]
                self.insert(code, char, self.root)
                encoded_text += code + ' '
        return encoded_text.strip()

    def decode(self, morse_code):
        decoded_text = ''
        for code in morse_code.split():
            node = self.root
            for symbol in code:
                if symbol == '.':
                    if node.left is None:
                        node.left = Node()
                    node = node.left
                elif symbol == '-':
                    if node.right is None:
                        node.right = Node()
                    node = node.right
            decoded_text += node.value
        return decoded_text

    def find(self, code):
        node = self.root
        for symbol in code:
            if symbol == '.':
                if node.left is None:
                    return None
                node = node.left
            elif symbol == '-':
                if node.right is None:
                    return None
                node = node.right
        return node.value

morse = MorseCode()
morse.insert('---..', 8, morse.root)
# Add the letter 'Ü' to the Morse code dictionary
#morse.MORSE_CODE_DICT['£'] = '..........'
# Encode and decode a message that includes the new letter
encoded_text = morse.encode('8')
print(encoded_text) # Output: "... --- ... / ..-- -... . .-. /"
decoded_text = morse.decode(encoded_text)
print(decoded_text) # Output: "SOS ÜBER"
print(morse.find('..-'))