from BST import BST
from rotations import left_rotate, right_rotate

tree = BST()
tree.insert(15)
tree.insert(6)
tree.insert(3)
tree.insert(7)
tree.insert(18)
tree.insert(17)
tree.insert(20)
tree.insert(2)
tree.insert(4)
tree.insert(13)
tree.insert(9)
print(tree)
print(tree.inorder())

right_rotate(tree, tree.root)
print(tree)
print(tree.inorder())