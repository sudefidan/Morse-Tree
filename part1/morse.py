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
                    '?':'..--..','&':'.-...', '/':'-..-.', 
                    '+': '.-.-.' , '-':'-....-','_':'..--.-',
                    '(':'-.--.', ')':'-.--.-', ':':'---...',';':'-.-.-.',
                    '’':'.----.', '”':'.-..-.','$':'...-..-',
                    '¿': '..-.-','¡': '--...-' ,'!': '-.-.--' }
    
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
    
    def find_value(self, code):
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
            print(prefix + node.value)
        if node.left:
            self.print_tree(node.left, prefix + 'l ')
        if node.right:
            self.print_tree(node.right, prefix + 'r ')

    """
    def isLeftChild(self):
        return self.parent and self.parent.left == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.right or self.left)"""









