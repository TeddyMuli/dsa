#!/usr/bin/python3
class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def pre_order(self, node):
        if node is None:
            return
        print(node.data, end=" ")
        self.pre_order(node.left)
        self.pre_order(node.right)

    def post_order(self, node):
        if node is None: return

        self.post_order(node.left)
        self.post_order(node.right)
        print(node.data, end=' ')

    def inorder(self, node):
        if node is None: return

        self.inorder(node.right)
        self.inorder(node.left)
        print(node.data, end=' ')
    
    def bfs(self, root):
        if root is None: return

        queue = [root]
        while queue:
            node = queue.pop(0)
            print(node.data, end=' ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

if __name__ == "__main__":
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.right.left = BinaryTree(4)
    print("Pre-order Traversal: ", end='')
    root.pre_order(root)
    print('\nPost-order Traversal: ', end='')
    root.post_order(root)
    print('\nIn-order Traversal: ', end='')
    root.inorder(root)
    print('\nLevel-order: ', end='')
    root.bfs(root)
    print('\n')
