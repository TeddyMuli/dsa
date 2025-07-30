#!/usr/bin/python3
class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def traverse(root):
    if root is None:
        return

    print(root.data, end=' ')
    traverse(root.left)
    traverse(root.right)

def delete(root, key):
    if root is None:
        return
    
    queue = [root]
    key_node = None
    last_node = None
    parent_last_node = None

    while queue:
        node = queue.pop(0)
        last_node = node
        if node.data == key:
            key_node = node
        if node.left:
            parent_last_node = node
            queue.append(node.left)
        if node.right:
            parent_last_node = node
            queue.append(node.right)

    if key_node:
        key_node.data = last_node.data
        if parent_last_node.right:
            parent_last_node.right = None
        else:
            parent_last_node.left = None
    else:
        print("\nKey not found!")

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)

    print("Before deletion: ", end='')
    traverse(root)

    delete(root, 1)

    print("\nAfter deletion: ", end='')
    traverse(root)
    print('\n')
