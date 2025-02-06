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

    def insert_at_beginning(self, data):
        current = self.head
        new_node = Node(data)
        current.prev = new_node
        new_node.next = current
        self.head = new_node

    def insert_at_end(self, data):
        current = self.tail
        new_node = Node(data)
        current.next = new_node
        new_node.prev = current
        self.tail = new_node

    def insert_at_position(self):
        pass

    def delete_node(self, key):
        head = self.head
        tail = self.tail

        if key == head.data:
            head.next.prev = None
            self.head = head.next

        if key == tail.data:
            tail.prev.next = None
            self.tail = tail.prev

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

    dl_list.insert_at_beginning(4)
    dl_list.forward_traverse()

    dl_list.insert_at_end(8)
    dl_list.backward_traverse()
