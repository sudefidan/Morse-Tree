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
    
    def insert2(self, morse_code, char):
        #self.left = MorseTree()
        #self.right = MorseTree()
        if not morse_code:
            self.value = char
            return
        elif morse_code[0] == '.':
            if not self.left:
                self.left = MorseTree()
            self.left.insert2(morse_code[1:], char)
        elif morse_code[0] == '-':
            if not self.right:
                self.right = MorseTree()
            self.right.insert2(morse_code[1:], char)
    
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

    def insert(self,root, word, morse):
        if len(word) == 0:
            self.root.morse = morse
            return
        if word[0] == '.':
            if root.left is None:
                root.left = Node()
            self.insert(root.left, word[1:], morse)
        else:
            if root.right is None:
                root.right = Node()
            self.insert(root.right, word[1:], morse)
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
    
    

    def isLeft(self,key):
        if self._get_key_path(key) == 'l':
            return True
        return False
    def isRight(self,key):
        path = self._get_key_path(key)
        if  path[:1]== 'r':
            return True
        return False
    def _get_key_path(self, key):
        # Convert the Morse code string to a path through the tree
        key_path = ''
        for char in key:
            if char == '.':
                key_path += 'l'
            else:
                key_path += 'r'
        return key_path

    def delete(self, value):
        # Start at the root of the Morse Tree
        current_node = self.root
        parent_node = None
        value_path = self._get_key_path(value)
        # Traverse the Morse Tree to find the node that contains the value
        for char in value_path:
            if char == 'L': #if char == '.':
                parent_node = current_node
                current_node = current_node.left
            else:
                parent_node = current_node
                current_node = current_node.right
        
        # If the value is not found in the Morse Tree, return None
        if current_node is None:
            return None
        
        # If the value is found in the Morse Tree, remove it from the tree and reorganize the tree accordingly
        if current_node.value == value:
            # If the node has no children, simply remove it from the tree
            if current_node.left is None and current_node.right is None:
                if parent_node is None:
                    self.root = None
                elif parent_node.left == current_node:
                    parent_node.left = None
                else:
                    parent_node.right = None
            # If the node has only one child, replace it with its child
            elif current_node.left is None:
                if parent_node is None:
                    self.root = current_node.right
                elif parent_node.left == current_node:
                    parent_node.left = current_node.right
                else:
                    parent_node.right = current_node.right
            elif current_node.right is None:
                if parent_node is None:
                    self.root = current_node.left
                elif parent_node.left == current_node:
                    parent_node.left = current_node.left
                else:
                    parent_node.right = current_node.left
            # If the node has two children, find the smallest node in the right subtree, replace the current node with it, and remove the smallest node from the right subtree
            else:
                smallest_node = current_node.right
                while smallest_node.left is not None:
                    parent_node = smallest_node
                    smallest_node = smallest_node.left
                current_node.value = smallest_node.value
                current_node.value = smallest_node.value
                if parent_node.left == smallest_node:
                    parent_node.left = smallest_node.right
                else:
                    parent_node.right = smallest_node.right
            return current_node.value
        else:
            return None

    def print_tree(self, node=None, prefix=''):
        if not node:
            node = self.root
        if node.value:
            print(prefix + node.value)
        if node.left:
            self.print_tree(node.left, prefix + 'l ')
        if node.right:
            self.print_tree(node.right, prefix + 'r ')

    def print_morsetree(self,node=None,prefix=None):
        if node is not None:
            if node is root:
                print(prefix + node.value)
            self.print_morsetree(node.left)
            key = self._get_key_path(node.value)
            print( key[:1]+ node.value)
            self.print_morsetree(node.right)



    
morse = MorseTree()
#morse.print_tree()
#print(morse.delete('.-'))
#print(morse.isLeft('.'))
#morse.print_tree(morse.root)
morse.insert2('.--.-.','@')
print(morse.find('.--.-.'))










