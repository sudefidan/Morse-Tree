class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class MorseTree:
    def __init__(self):
        self.root = Node('')
        self.dict = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
    
        for letter, code in self.dict.items():
            self.insert(code,letter)
        
    def insert(self, code, value):
        node = self.root
        for c in code:
            if c == ".":
                if node.left is None:
                    node.left = Node('')
                node = node.left
            elif c == "-":
                if node.right is None:
                    node.right = Node('')
                node = node.right
        node.value = value

    def encode(self, text):
        encoded_text = ''
        for char in text.upper():
            if char in self.dict:
                encoded_text += self.dict[char] + ' '
        return encoded_text.strip()

    def decode(self, code):
        decoded = ""
        for word in code.split("/"):
            for letter in word.split():
                node = self.root
                for c in letter:
                    if c == ".":
                        node = node.left
                    elif c == "-":
                        node = node.right
                decoded += node.value
            decoded += " "
        return decoded.strip()


# Example usage
tree = MorseTree()
dec = '-.--.-'
enc = ')'
decode_message = tree.decode(dec)
print(decode_message)  
encode_message = tree.encode(enc)
print(encode_message)