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
        self.tail = None

    def forward_traverse(self):
        current = self.head
        print('Forward Traversal:', end=' ')

        while current:
            print(str(current.data) + '->', end=" ")
            current = current.next

        print('None')

    def backward_traverse(self):
        current = self.tail
        print('Backward Traversal:', end=' ')
        
        while current:
            print(str(current.data) + '->', end=' ')
            current = current.prev

        print('None')

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
    second = Node(2)
    third = Node(3)
    dl_list.head.next = second
    second.prev = dl_list.head
    second.next = third
    third.prev = second
    dl_list.tail = third

    dl_list.forward_traverse()
    dl_list.backward_traverse()
