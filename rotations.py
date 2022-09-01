from BST import BST


def left_rotate(tree, node):
    """
    performs a left-rotation given a BST tree and the pointer to node. Assumes that node.right is not null.
    """
    y = node.right
    node.right = y.left

    if y.left:
        node.right.parent = node

    y.parent = node.parent

    # link node's parent to y.
    if y.parent is None:
        tree.root = y

    elif node.parent.left == node:
        node.parent.left = y

    else:
        node.parent.right = y

    y.left = node
    node.parent = y


def right_rotate(tree, node):
    """
    performs a right rotation on tree given a pointer to node. Assumes node.left is not null.
    """
    x = node.left
    node.left = x.right

    if x.right:
        x.right.parent = node

    x.parent = node.parent

    # link node's parent to x
    if x.parent is None:
        tree.root = x

    elif node.parent.left == node:
        node.parent.left = x

    else:
        node.parent.right = x

    x.right = node
    node.parent = x