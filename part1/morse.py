class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    """This method will check to see if the tree already has a root. 
    If there is not a root then put will create a new TreeNode and install it as the root of the tree.
     If a root node is already in place then put calls the private, recursive, helper function _put to search the tree"""
    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size = self.size + 1

    """This method is to search the tree according to the following algorithm: 
    1)  Starting at the root of the tree, search the binary tree comparing the new key to the key in the current node. 
        If the new key is less than the current node, search the left subtree. 
        If the new key is greater than the current node, search the right subtree.
    2)  When there is no left (or right) child to search, we have found the position in the tree where the new node should be installed.
    3)  To add a node to the tree, create a new TreeNode object and insert the object at the point discovered in the previous step."""
    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key,val,parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key,val,parent=currentNode)

    """With the put method defined, we can easily overload the [] operator for assignment by having the __setitem__ method. 
    This allows us to write Python statements like myZipTree['Plymouth'] = 55446, just like a Python dictionary."""
    def __setitem__(self,k,v):
        self.put(k,v)

    """Implementation of  the retrieval of a value for a given key.
    It searches the tree recursively until it gets to a non-matching leaf node or finds a matching key.
    When a matching key is found, the value stored in the payload of the node is returned."""
    def get(self,key):
        if self.root:
            res = self._get(key,self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    """This method returns a TreeNode to get, this allows _get to be used as a flexible helper method 
    for other BinarySearchTree methods that may need to make use of other data from the TreeNode besides the payload."""
    def _get(self,key,currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key,currentNode.leftChild)
        else:
            return self._get(key,currentNode.rightChild)

    """By implementing the __getitem__ method we can write a Python statement that looks just like we are accessing a dictionary, 
    when in fact we are using a binary search tree, for example z = myZipTree['Fargo']. 
    As you can see, all the __getitem__ method does is call get."""
    def __getitem__(self,key):
        return self.get(key)
    
    """Using get, we can implement the in operation by writing a __contains__ method for the BinarySearchTree. 
    The __contains__ method will simply call get and return True if get returns a value, or False if it returns None. 
    Recall that __contains__ overloads the in operator and allows us to write statements such as:
    if 'Northfield' in myZipTree:
        print("oom ya ya")"""
    def __contains__(self,key):
        if self._get(key,self.root):
            return True
        else:
            return False
    
    """Deletion of key
    First we need to find the node to delete by searching the tree. 
    If the tree has more than one node we search using the _get method to find the TreeNode that needs to be removed. 
    If the tree only has a single node, that means we are removing the root of the tree, 
    but we still must check to make sure the key of the root matches the key that is to be deleted.
     In either case if the key is not found the del operator raises an error."""
    def delete(self,key):
        if self.size > 1:
            nodeToRemove = self._get(key,self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size-1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')
        
    def remove(self,currentNode):
        if currentNode.isLeaf(): #leaf
            """If the node to be deleted has no children
            delete the node and remove the reference to this node in the parent. """
            if currentNode == currentNode.parent.leftChild:
               currentNode.parent.leftChild = None
            else:
               currentNode.parent.rightChild = None
            
        elif currentNode.hasBothChildren(): #interior
            """If the node to be deleted has two children: 
            it is unlikely that we can simply promote one of them to take the node’s place. 
            We can, however, search the tree for a node that can be used to replace the one scheduled for deletion.
            What we need is a node that will preserve the binary search tree relationships for both of the existing left and right subtrees.
            The node that will do this is the node that has the next-largest key in the tree. 
            We call this node the successor, the successor is guaranteed to have no more than one child, 
            so we know how to remove it using the two cases for deletion that we have already implemented. 
            Once the successor has been removed, we simply put it in the tree in place of the node to be deleted."""
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload

        else: # this node has one child
            """If the node to be deleted has only one child:
            1)  If the current node is a left child:
                we only need to update the parent reference of the left child to point to the parent of the current node, 
                and then update the left child reference of the parent to point to the current node’s left child.
            2)  If the current node is a right child:
                we only need to update the parent reference of the left child to point to the parent of the current node,
                and then update the right child reference of the parent to point to the current node’s left child.
            3)  If the current node has no parent, it must be the root. 
                In this case we will just replace the key, payload, leftChild, and rightChild data by calling the replaceNodeData method on the root."""
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                        currentNode.leftChild.payload,
                                        currentNode.leftChild.leftChild,
                                        currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                        currentNode.rightChild.payload,
                                        currentNode.rightChild.leftChild,
                                        currentNode.rightChild.rightChild)

        

    def __delitem__(self,key):
        self.delete(key)

"""The root of the binary search tree"""
class TreeNode: 
    
    def __init__(self,key,val,left=None,right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            """If the node has a right child, then the successor is the smallest key in the right subtree."""
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                """If the node has no right child and is the left child of its parent, then the parent is the successor."""
                if self.isLeftChild():
                    succ = self.parent
                else:
                    """If the node is the right child of its parent, and itself has no right child, then the successor to this node is the successor of its parent, excluding this node."""
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ
    
    """To find the minimum key in a subtree"""
    def findMin(self):
        current = self
        """the minimum valued key in any binary search tree is the leftmost child of the tree"""
        while current.hasLeftChild():
            current = current.leftChild
        return current
    
    """To remove the successor"""
    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

"""
            
class Node:
    def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
    
    # Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()


# Use the insert method to add nodes
root = Node("Start")

root.left=Node("E")
root.right=Node("T")

root.left.left=Node("I")
root.left.right=Node("A")

root.right.left=Node("N")
root.right.right=Node("M")

root.left.left.left=Node("S")
root.left.left.right=Node("U")

root.left.right.left=Node("R")
root.left.right.right=Node("W")

root.right.left.left=Node("D")
root.right.left.right=Node("K")

root.right.right.left=Node("G")
root.right.right.right=Node("O")

root.left.left.left.left=Node("H")
root.left.left.left.right=Node("V")

root.left.left.right.left=Node("F")
root.left.left.right.right=Node("")

root.left.right.left.left=Node("L")
root.left.right.left.right=Node("")

root.left.right.right.left=Node("P")
root.left.right.right.right=Node("J")

root.right.left.left.left=Node("B")
root.right.left.left.right=Node("X")

root.right.left.right.left=Node("C")
root.right.left.right.right=Node("Y")

root.right.right.left.left=Node("Z")
root.right.right.left.right=Node("Q")

root.right.right.right.left=Node("")
root.right.right.right.right=Node("")


root.left.left.left.left.left=Node(5)
root.left.left.left.left.right=Node(4)

root.left.left.left.right.left=Node("")
root.left.left.left.right.right=Node(3)

root.left.left.right.left.left=Node("")
root.left.left.right.left.right=Node("")

root.left.left.right.right.left=Node("")
root.left.left.right.right.right=Node(2)


root.left.right.left.left.left=Node("")
root.left.right.left.left.right=Node("")

root.left.right.left.right.left=Node("+")
root.left.right.left.right.right=Node("")


root.left.right.right.left.left=Node("")
root.left.right.right.left.right=Node("")

root.left.right.right.right.left=Node("")
root.left.right.right.right.right=Node(1)

root.right.left.left.left.left=Node(6)
root.right.left.left.left.right=Node("=")

root.right.left.left.right.left=Node("/")
root.right.left.left.right.right=Node("")

root.right.left.right.left.left=Node("")
root.right.left.right.left.right=Node("")

root.right.left.right.right.left=Node("")
root.right.left.right.right.right=Node("")

root.right.right.left.left.left=Node(7)
root.right.right.left.left.right=Node("")

root.right.right.left.right.left=Node("")
root.right.right.left.right.right=Node("")

root.right.right.right.left.left=Node(8)
root.right.right.right.left.right=Node("")

root.right.right.right.right.left=Node(9)
root.right.right.right.right.right=Node(0)

root.PrintTree()

"""
mytree = BinarySearchTree()
mytree[3]="red"
mytree[4]="blue"
mytree[6]="yellow"
mytree[2]="at"

print(mytree[6])
print(mytree[2])
