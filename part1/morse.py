#SUDE FIDAN - 21068639

#represents each node of Morse Tree
class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

#Morse Binary Tree classes for encoding and decoding morse code
class MorseTree:
    
    def __init__(self):
        #create a root
        self.root = Node('')
        #populate tree with dictionary
        self.populate()
        
    #poulate the tree with symbols
    def populate(self):
        self.dict = { 'A':'.-', 'B':'-...','C':'-.-.', 
                    'D':'-..', 'E':'.','F':'..-.', 
                    'G':'--.', 'H':'....','I':'..', 
                    'J':'.---', 'K':'-.-','L':'.-..', 
                    'M':'--', 'N':'-.','O':'---', 
                    'P':'.--.', 'Q':'--.-','R':'.-.',
                    'S':'...', 'T':'-','U':'..-', 
                    'V':'...-', 'W':'.--','X':'-..-',
                    'Y':'-.--', 'Z':'--..','1':'.----', 
                    '2':'..---', '3':'...--','4':'....-',
                    '5':'.....', '6':'-....','7':'--...', 
                    '8':'---..', '9':'----.','0':'-----',
                    ',':'--..--', '.':'.-.-.-','?':'..--..',
                    '&':'.-...', '/':'-..-.', '+': '.-.-.' ,
                    '-':'-....-','_':'..--.-','(':'-.--.', 
                    ')':'-.--.-', ':':'---...',';':'-.-.-.',
                    '’':'.----.', '”':'.-..-.','$':'...-..-',
                    '¿': '..-.-','¡': '--...-' ,'!': '-.-.--',
                    ' ':'/' }

        #add dictionary to tree
        for letter, code in self.dict.items():
            self.insert(code,letter)

    #check if the tree is empty
    def is_empty(self):
        return self.root is None
    
    #check if the tree is not empty
    def is_not_empty(self):
        return self.root is not  None

    #adds new symbols to tree and dictionary
    def insert(self, code, value):
        node = self.root
        for c in code:
            #dot means left child, dash means right child
            if c == ".":
                #if there is no left child, create a node
                if node.left is None:
                    node.left = Node('')
                node = node.left
            elif c == "-":
                #if there is no right child, create a node
                if node.right is None:
                    node.right = Node('')
                node = node.right
        node.value = value
        #add it to dictionary
        self.dict[value]=code
    
    #converts text to morse
    #E.g. Input: Sude Fidan ==> Output: ... ..- -.. . / ..-. .. -.. .- -.
    def encode(self, text):
        encoded_text = ''
        #convert letters to upper letter , numbers and symbols won't be affected
        for char in text.upper():
            #check if char existed in dictionary
            if char in self.dict:
                #translate to morse
                encoded_text += self.dict[char] + ' '
        return encoded_text.strip()

    #converts morse to text
    #E.g Input: .-- . / .-.. --- ...- . / .--. -.-. / -.-.-- ==> Output: WE LOVE PC !
    def decode(self, code):
        decoded = ""
        #split the words: / means space between words in morsecode
        for word in code.split("/"):
            for letter in word.split():
                node = self.root
                for c in letter:
                    #dot means left child, dash means right child
                    if c == ".":
                        node = node.left
                    elif c == "-":
                        node = node.right
                decoded += node.value
            #add each word to text
            decoded += " "
        return decoded.strip()
    
    #finding a symbol
     #E.g Input:.- ==> Output:A
    def find(self, code):
        node = self.root
        for symbol in code:
            #dot means left child, dash means right child
            if symbol == '.':
                #if its leaf node return none
                if node.left is None:
                    return None
                node = node.left
            elif symbol == '-':
                #if its leaf node return none
                if node.right is None:
                    return None
                node = node.right
        return node.value

    #prints the whole tree structure
    def print_tree(self, node=None, prefix=''):
        if not node:
            node = self.root
        if node.value:
            #arrange the print
            print( prefix[:-2].replace('r',' ').replace('l', ' ')+ prefix[-2:] + node.value)
        if node.left:
            #l means left child of the root
            self.print_tree(node.left, prefix + 'l ')
        if node.right:
            #r means right child of the root
            self.print_tree(node.right, prefix + 'r ')




