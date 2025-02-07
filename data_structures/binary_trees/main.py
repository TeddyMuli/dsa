#!/usr/bin/env python3
''' Python module for a binary tree
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        
        def _insert_recursive(node, data):
            if data < node.data:
                if node.left is None:
                    node.left = Node(data)
                else:
                    _insert_recursive(node.left, data)
            else:
                if node.right is None:
                    node.right = Node(data)
                else:
                    _insert_recursive(node.right, data)
        
        _insert_recursive(self.root, data)

    def traverse(self):
        def _traverse_recursive(node, level=0, prefix='Root: '):
            if node is not None:
                print(' ' * level + prefix + str(node.data))
                if node.left or node.right:
                    if node.left:
                        _traverse_recursive(node.left, level + 1, 'L---')
                    if node.right:
                        _traverse_recursive(node.right, level + 1, 'R---')
        
        _traverse_recursive(self.root)

if __name__ == '__main__':
    tree = BinaryTree()
    values = [5, 5, 6, 2, 9, 1, 3]

    for value in values:
        tree.insert(value)

    tree.traverse()
