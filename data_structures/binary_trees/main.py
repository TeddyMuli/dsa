#!/usr/bin/python3
''' Python module to learn binary trees
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_node(self, data):
        if self.root is None:
            self.root = Node(data)
            return
                       
        def _insert_node_recursive(node, data):
            if data < node.data:
                if node.left is None:
                    node.left = Node(data)
                else:
                   _insert_node_recursive(node.left, data)
            else:
                if node.right is None:
                    node.right = Node(data)
                else:
                    _insert_node_recursive(node.right, data)

        _insert_node_recursive(self.root, data)

    def pre_order_traversal(self):
        def _pre_order_traversal_recursive(node, level=0, prefix='Root: '):
            if node:
                print(' ' * level + prefix + str(node.data))
                if node.left or node.right:
                    if node.left:
                        _pre_order_traversal_recursive(node.left, level+1, prefix='L---')
                    if node.right:
                        _pre_order_traversal_recursive(node.right, level+1, prefix='R---')

        _pre_order_traversal_recursive(self.root)

    def remove_node(self, key):
        parent = None
        def _find_node_recursive(node, parent=self.root):
            if node:
                if node.data == key:
                    parent = parent
                    return node
                elif node.left or node.right:
                    if node.left:
                        _find_node_recursive(node.left, node)
                    if node.right:
                        _find_node_recursive(node.right, node)
            else:
                return None
            
        node = _find_node_recursive(self.root)
        if node:
            left = node.left
            right = node.right
            parent.right = right
            parent.left = left

    def reverse(self):
        pass


if __name__ == '__main__':
    b_tree = BinaryTree()
    #b_tree.root = Node(0)
    b_tree.insert_node(3)
    b_tree.insert_node(2)
    b_tree.insert_node(1)
    b_tree.insert_node(4)
    b_tree.pre_order_traversal()
    b_tree.remove_node(2)
    b_tree.pre_order_traversal()
