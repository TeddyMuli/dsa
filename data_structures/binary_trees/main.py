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
        
    def traverse(self):
        if self.root is None:
            return
        