#!/usr/bin/env python3
""" Create a binary tree with 4 nodes
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

firstNode = Node(2)
secondNode = Node(3)
thirdNode = Node(4)
fourthNode = Node(5)

firstNode.left = secondNode
firstNode.right = thirdNode
secondNode.left = fourthNode

