#!/usr/bin/env python3
""" Traversal of a binary Tree
    1. Depth First Traversal:
        i. Preorder Traversal
        ii. Inorder Traversal
        iii. Postorder Traversal
    2. Breadth First Traversal
        i. Level Order Traversal
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def pre_order(node):
    if node is None:
        return
    
    print(node.data, end=' ')
    pre_order(node.left)
    pre_order(node.right)

def in_order(node):
    if node is None:
        return
    
    in_order(node.left)
    print(node.data, end=' ')
    in_order(node.right)

def post_order(node):
    if node is None:
        return
    
    post_order(node.left)
    post_order(node.right)
    print(node.data, end=' ')

def bfs(root):
    if root is None:
        return

    queue = [root]
    while(queue):
        node = queue.pop(0)
        print(node.data, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

if __name__ == "__main__":
    root = Node(2)
    root.left = Node(3)
    root.right = Node(4)
    root.left.left = Node(5)

    print('In order traversal: ', end=' ')
    in_order(root)
    print("\nPre-order DFS: ", end='')
    pre_order(root)
    print("\nPost-order DFS: ", end='')
    post_order(root)
    print("\nLevel order: ", end='')
    bfs(root)
