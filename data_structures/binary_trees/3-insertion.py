#!/usr/bin/env python3
""" Script to implement insertion in a binary tree
"""
from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)

    queue = deque([root])

    while queue:
        temp = queue.popleft()

        if temp.left is None:
            temp.left = Node(value)
            break
        else:
            queue.append(temp.left)

        if temp.right is None:
            temp.right = Node(value)
            break
        else:
            queue.append(temp.right)
    
    return root

def in_order(node):
    if node is None:
        return
    
    in_order(node.left)
    print(node.data, end=' ')
    in_order(node.right)

if __name__ == "__main__":
    root = Node(2)
    root.left = Node(3)
    root.right = Node(4)
    root.left.left = Node(5)

    print('In-order traversal before insertion: ', end=' ')
    in_order(root)
    print()

    value = 6
    root = insert(root, value)

    print("Inorder traversal after insertion: ", end="")
    in_order(root)
    print()
