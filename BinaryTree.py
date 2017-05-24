class Node:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.data = val


def in_order_print(root):
    if not root:
        return
    in_order_print(root.l_child)
    print(root.data)
    in_order_print(root.r_child)


def pre_order_print(root):
    if not root:
        return
    print(root.data)
    pre_order_print(root.l_child)
    pre_order_print(root.r_child)


def binary_insert(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.l_child is None:
                root.l_child = node
            else:
                binary_insert(root.l_child, node)
        else:
            if root.r_child is None:
                root.r_child = node
            else:
                binary_insert(root.r_child, node)


def lookup(root, item):
    if root is None:
        return None
    if item.data < root.data:
        if root.l_child is None:
            return None
        return lookup(root.l_child, item)
    elif item.data > root.data:
        if root.data is None:
            return None
        return lookup(root.r_child, item)
    else:
        return root


r = Node(3)
binary_insert(r, Node(7))
binary_insert(r, Node(1))
binary_insert(r, Node(5))
binary_insert(r, Node(2))
binary_insert(r, Node(4))
binary_insert(r, Node(6))
binary_insert(r, Node(8))
binary_insert(r, Node(9))
binary_insert(r, Node(12))
binary_insert(r, Node(11))
binary_insert(r, Node(10))

print("Inorder Traversal:")
in_order_print(r)
print("Preorder Traversal")
pre_order_print(r)

result = lookup(r, Node(9))
if result == None:
    print("Node not in the Tree...")
else:
    print("Node Found...",result.data)