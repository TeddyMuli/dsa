#!/usr/bin/python3
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def bft(root):
    if root is None:
        return
    
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.data, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

def delete(root, key):
    if root is None:
        return
    
    if not root.left and not root.right:
        return None if root.data == key else root

    queue = [root]
    last_node = None
    key_node = None
    parent_last = None

    while queue:
        last_node = queue.pop(0)

        if last_node.data == key:
            key_node = last_node
        if last_node.left:
            parent_last = last_node
            queue.append(last_node.left)
        if last_node.right:
            parent_last = last_node
            queue.append(last_node.right)

    if key_node:
        key_node.data = last_node.data
        if parent_last.right == last_node:
            parent_last.right = None
        else:
            parent_last.left = None
    else:
        print('\nKey not found!')

if __name__ == "__main__":
    root = Node(1)
    root.right = Node(3)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(7)
    root.left.left.right = Node(6)

    print("Before Deletion: ",end='')
    bft(root)
    delete(root, 12)
    print("\nAfter Deletion: ",end='')
    bft(root)
    print('\n')
