"""
Implementation of a Binary Search Tree with the Node class defined with parent, left child, right child, and key
value.
    - parent is the pointer to the parent node of each TreeNode.
    - left  is the pointer to the left child of each TreeNode
    - right is the pointer to the right child of each TreeNode.
    - key is the value of the TreeNode.

ASSUMES THE VALUES IN THE BST ARE UNIQUE.

Consists of the following methods:
    - insert(x): inserts the key x into the tree
    - serialize(): performs a serialized preorder traversal on the tree. The default for displaying a tree.
    - transplant(u, v): replaces the BST rooted at u with the BST rooted at v. Helper method for delete.
    - delete(x): deletes the node x from the tree and adjusts the tree accordingly.
    - search(x): searches the tree for node x, returns -1 if not found.
    - successor(x): returns the inorder successor to the node x.
    - inorder(): performs  and returns tje inorder traversal of the BST.
"""


class Node:
    def __init__(self, key=None, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent


class BST:
    def __init__(self, root=None):
        self.root = root

    def __str__(self):
        return self.serialize()

    def serialize(self):
        root = self.root

        def recurse(root, string):
            if root is None:
                string += 'None,'
            else:
                string += str(root.key) + ','
                string = recurse(root.left, string)
                string = recurse(root.right, string)
            return string

        serial = recurse(root, '')

        if serial[-1] == ",":
            serial = serial[:-1]

        return serial

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)

        else:
            data = Node(data)
            x = self.root
            prev = None

            while x:
                prev = x

                if data.key < x.key:
                    x = x.left

                else:
                    x = x.right

            data.parent = prev

            if data.key < prev.key:
                prev.left = data
            else:
                prev.right = data

    def transplant(self, u, v):
        u = u.root
        v = v.root
        if u is None:
            self.root = v

        else:
            if u.parent.left == u:
                u.parent.left = v
            else:
                u.parent.right = v

            if v:
                v.parent = u.parent

    def delete(self, node):
        """
        5 subcases for this:
            1) node is a leaf node.
                - simply delete node by setting node.parent appropriate child to none.
            2) node has only a left child.
                - transplant node with node.left
            3) node has only a right child
                - transplant node with node.right
            4) node has both left and right children
                - let y be in the inorder successor of node.
                4a) if y == node.right:
                    - transplant node with y
                    - set y.left to equal to node.left
                    - set node.left.parent to equal to y.

                4b) else:
                    - transplant y with its right child.
                    - set y.right to point to node.right, set r.parent to be y
                    - transplant y with node.
                    - set y.left to be node.left
                    - set y.left's parent to be y.
        """
        pass

    def search(self, target):
        root = self.root

        while root and target != root.key:
            if target < root.key:
                root = root.left

            else:
                root = root.right

        return BST(root)

    def successor(self, node):
        node = self.search(node)
        root = node.root

        if root.right:
            r = root.right

            while r.left:
                r = r.left

            return BST(r)

        else:
            p = root.parent

            while p and root == p.right:
                root = p
                p = root.parent

            return BST(p)

    def inorder(self):
        root = self.root
        order = []

        def helper(root, order):
            if root:
                helper(root.left, order)
                order.append(root.key)
                helper(root.right, order)

        helper(root, order)
        return order
