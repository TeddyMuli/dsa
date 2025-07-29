#!/usr/bin/python3
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def traverse(root):
    if not root:
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
    root.right = Node(3)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(7)
    root.left.left.right = Node(6)

    print("Before inverting: ", end='')
    traverse(root)
    invert(root)
    print("\nAfter inverting: ", end='')
    traverse(root)
    print('\n')
