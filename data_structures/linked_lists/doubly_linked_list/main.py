#!/usr/bin/env python3
''' Python module for double linked lists
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        pass

    def insert_at_beginning(self):
        pass

    def insert_at_end(self):
        pass

    def insert_at_position(self):
        pass

    def delete_node(self):
        pass

if __name__ == "__main__":
    dl_list = DoublyLinkedList()
    dl_list.head = Node(1)
    
