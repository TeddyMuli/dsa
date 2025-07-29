#!/usr/bin/python3
class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def pre_order(self, node):
        if node is None: return

        print(node.data, end=' ')
        self.pre_order(node.left)
        self.pre_order(node.right)

    def insert(self, root, value):
        if root is None:
            self.data = value
            return

        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.left is None:
                node.left = BinaryTree(value)
                break
            else:
                queue.append(node.left)

            if node.right is None:
                node.right = BinaryTree(value)
                break
            else:
                queue.append(node.right)

if __name__ == "__main__":
    root = BinaryTree(1)
    print("Before Insertion: ", end='')
    root.pre_order(root)
    root.insert(root, 2)
    print("\nAfter Insertion: ", end='')
    root.pre_order(root)
    print('\n')
