class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class MorseTree:
    def __init__(self):
        self.root = TreeNode('')
        self._populate_tree()

    def _populate_tree(self):
        # The Morse code tree structure
        morse_dict = {'E': '.', 'T': '-', 'I': '..',
                      'A': '.-', 'N': '-.', 'M': '--',
                      'S': '...', 'U': '..-', 'R': '.-.',
                      'W': '.--', 'D': '-..', 'K': '-.-',
                      'G': '--.', 'O': '---', 'H': '....',
                      'V': '...-', 'F': '..-.', ' ': '/',
                      'L': '.-..', 'P': '.--.', 'J': '.---',
                      'B': '-...', 'X': '-..-', 'C': '-.-.',
                      'Y': '-.--', 'Z': '--..', 'Q': '--.-'}
        for letter, code in morse_dict.items():
            node = self.root
            for symbol in code:
                if symbol == '.':
                    if node.left is None:
                        node.left = TreeNode('')
                    node = node.left
                elif symbol == '-':
                    if node.right is None:
                        node.right = TreeNode('')
                    node = node.right
            node.value = letter

    def decode(self, morse_code):
        node = self.root
        message = ''
        for symbol in morse_code:
            if symbol == '.':
                node = node.left
            elif symbol == '-':
                node = node.right
            else:
                message += node.value
                node = self.root
        message += node.value
        return message
    def insert(self, code, value):
        node = self.root
        for c in code:
            if c == ".":
                if node.left is None:
                    node.left = TreeNode('')
                node = node.left
            elif c == "-":
                if node.right is None:
                    node.right =TreeNode('')
                node = node.right
        node.value = value
        
    def _find_code(self, node, value):
        if node is None:
            return ""
        if node.value == value:
            return ""
        left_code = self._find_code(node.left, value)
        if left_code is not None:
            return "." + left_code
        right_code = self._find_code(node.right, value)
        if right_code is not None:
            return "-" + right_code
        return None

    def encode(self, text):
        encoded = ""
        for c in text.upper():
            node = self.root
            if c == " ":
                encoded += "/"
                continue
            code = self._find_code(node, c)
            encoded += code + " "
        return encoded.strip()


# Example usage
tree = MorseTree()

tree.insert("..........", "21")
dec = '..........'
enc = '21'
decode_message = tree.decode(dec)
#print(decode_message)  
encode_message = tree.encode(enc)
print(encode_message)