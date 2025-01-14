#!/usr/bin/env python3
""" Search a binary tree
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def search_by_dfs(root, value):
    if root is None:
        return False
    
    if root.data == value:
        return True
    
    left_res = search_by_dfs(root.left, value)
    right_res = search_by_dfs(root.right, value)

    return right_res or left_res

if __name__ == "__main__":
    root = Node(2)
    root.left = Node(3)
    root.right = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(6)

    value = 9
    if search_by_dfs(root, value):
        print(f"{value} is found in the binary tree")
    else:
        print(f"{value} is not found in the binary tree")

