#!/usr/bin/python3
class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def insert(root, data):
    if root is None:
        return Node(data)
    
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)

    return root

def traverse(root):
    if root is None:
        return
    
    print(root.data, end=' ')
    traverse(root.left)
    traverse(root.right)

if __name__ == "__main__":
    root = Node(0)
    insert(root, 1)
    insert(root, 2)
    insert(root, 3)
    insert(root, 4)
    print("Binary Tree: ", end='')
    traverse(root)
    print()
