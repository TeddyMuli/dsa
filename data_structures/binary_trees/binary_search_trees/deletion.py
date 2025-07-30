#!/usr/bin/python3
class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def traverse(root):
    if root is None:
        return
    
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.data, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

def get_min_node(node):
    while node.left:
        node = node.left
    return node

def delete(root, key):
    if root is None:
        return None
    
    if key < root.data:
        root.left = delete(root.left, key)
    elif key > root.data:
        root.right = delete(root.right, key)
    else:
        if not root.right and not root.left:
            return None
        
        if not root.left:
            return root.right
        
        if not root.right:
            return root.left
        
        successor = get_min_node(root.right)
        root.data = successor.data
        root.right = delete(root.right, successor.data)
    return root

if __name__ == "__main__":
    root = Node(3)
    root.left = Node(2)
    root.left.left = Node(1)
    root.right = Node(4)
    root.right.right = Node(5)

    print("Before deletion: ", end='')
    traverse(root)
    delete(root, 4)
    print("\nAfter deletion: ", end='')
    traverse(root)
    print()
