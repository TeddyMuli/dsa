#!/usr/bin/python3
class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def search(self, root, key):
        if root is None:
            return False
        
        if root.data == key:
            print(f"{key} is in the binary tree!")
            return True
        
        found_left = self.search(root.left, key)
        found_right = self.search(root.right, key)

        if not found_left and not found_right and root == self:
            print(f"{key} is not in binary tree")

        return found_left or found_right
    
    def search_bfs(self, root, key):
        if root is None:
            return False
        
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.data == key:
                print(f"\n{key} is in the binary tree!")
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        print(f"{key} is not in binary tree")


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

    root.search_bfs(root, 1)
    root.search_bfs(root, 4)
