"""
Implementation of a Binary Search Tree with the TreeNode class defined with parent, left child, right child, and key
value.
    - parent is the pointer to the parent node of each TreeNode.
    - left  is the pointer to the left child of each TreeNode
    - right is the pointer to the right child of each TreeNode.
    - key is the value of the TreeNode.

Consists of the following methods:
    - insert(x): inserts the key x into the tree.
    - delete(x): deletes the node x from the tree and adjusts the tree accordingly.
    - search(x): searches the tree for node x, returns -1 if not found.
    - inorder(): performs an inorder traversal of the BST.
"""


class BST:
    def __init__(self, key=None, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = None

    def insert(self, node):
        pass

    def delete(self, node):
        pass

    def search(self, node):
        pass

    def inorder(self):
        pass
