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

def invert(root):
    if root is None:
        return
    
    root.left, root.right = invert(root.right), invert(root.left)
    return root

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)

    print("Before inversion: ", end='')
    traverse(root)

    invert(root)

    print("\nAfter inversion: ", end='')
    traverse(root)
    print('\n')
