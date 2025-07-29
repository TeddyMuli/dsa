#!/usr/bin/python3
class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

if __name__ == "__main__":
    first = BinaryTree(1)
    second = BinaryTree(1)
    third = BinaryTree(3)
    fourth = BinaryTree(4)

    first.left = second
    first.right = third
    third.left = fourth
