#!/usr/bin/python3
class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def search(self, node, value):
        if node is None:
            return False
        if node.data == value:
            print(f"\n{value} is in the binary tree")
            return True
        found_left = self.search(node.left, value)
        found_right = self.search(node.right, value)
        if not found_left and not found_right and node == self:
            print(f"{value} is NOT in the binary tree")
        return found_left or found_right

    def insert(self, data):
        if self is None:
            self.data = data
            return
        
        queue = [self]
        while queue:
            node = queue.pop(0)
            if node.left is None:
                node.left = BinaryTree(data)
                break
            else:
                queue.append(node.left)

            if node.right is None:
                node.right = BinaryTree(data)
                break
            else:
                queue.append(node.right)

    def pre_order(self, node):
        if node is None:
            return
        
        print(node.data, end=' ')
        self.pre_order(node.left)
        self.pre_order(node.right)

if __name__ == "__main__":
    root = BinaryTree(1)
    root.insert(2)
    root.insert(3)
    root.pre_order(root)

    root.search(root, 1)
    root.search(root, 4)
