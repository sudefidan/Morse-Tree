class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
        def getValue(self):
            return self.value
        def getLeft(self):
            return self.left
        def getRight(self):
            return self.right
        def setValue(self,value):
            self.value = value 
        def setLeft(self,left):
            self.left=left
        def setRight(self,right):
            self.right=right

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
                    '0':'-----', ',':'--..--', '.':'.-.-.-',
                    '?':'..--..','&':'.-...', '/':'-..-.', 
                    '+': '.-.-.' , '-':'-....-','_':'..--.-',
                    '(':'-.--.', ')':'-.--.-', ':':'---...',';':'-.-.-.',
                    '’':'.----.', '”':'.-..-.','$':'...-..-',
                    '¿': '..-.-','¡': '--...-' ,'!': '-.-.--' }
    
        for letter, code in self.dict.items():
            self.insert(code,letter)

    def is_empty(self):
        return self.root is None
    
    def is_not_empty(self):
        return self.root is not  None

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
        self.dict[value]=code
    
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

    def print_tree(self, node=None, prefix=''):
        if not node:
            node = self.root
        if node.value:
            print( prefix[:-2].replace('r',' ').replace('l', ' ')+ prefix[-2:] + node.value)
        if node.left:
            self.print_tree(node.left, prefix + 'l ')
        if node.right:
            self.print_tree(node.right, prefix + 'r ')


    
morse = MorseTree()
#morse.insert('.--.-.','@')

#print(morse.find('.--.-.'))
#morse.delete('@')
#print(morse.find('.--.-.'))

#morse.print_tree(morse.root)











