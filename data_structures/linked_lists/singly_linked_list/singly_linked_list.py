#!/usr/bin/env python3
""" Python module to demonstrate a singly linked list
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        current = self.head
        while current:
            print(str(current.data) + "->", end=" ")
            current = current.next

        print("None")

    def insert_at_beginning(self, data):
        current = self.head
        new_node = Node(data)
        new_node.next = current
        self.head = new_node

    def insert_at_end(self, data):
        current = self.head
        new_node = Node(data)

        while current:
            if current.next == None:
                current.next = new_node
                break

            current = current.next

    def delete_node(self, key):
        current = self.head

        if current.data == key:
            self.head = current.next
            return

        while current.next:
            if current.next.data == key:
                current.next = current.next.next
                break

            current = current.next

        if current == None:
            return
        
    def insert_at_position(self, data, position):
        current = self.head
        new_node = Node(data)
        count = 1

        if position == 0:
            self.insert_at_beginning(data)
            return

        while current.next:
            if count == position:
                new_node.next = current.next
                current.next = new_node
                break
            
            count += 1
            current = current.next

        if current.next == None:
            self.insert_at_end(data)

    def update(self, key, data):
        current = self.head

        while current:
            if current.data == key:
                current.data = data
                break

            current = current.next

        if current == None:
            return
        
    def reverse(self):
        current = self.head
        previous = None

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous

if __name__ == '__main__':
    l_list = LinkedList()
    l_list.head = Node(1)
    second = Node(2)
    third = Node(3)

    l_list.head.next = second
    second.next = third
    l_list.traverse()
    l_list.insert_at_beginning(5)
    l_list.traverse()
    l_list.insert_at_end(8)
    l_list.traverse()
    l_list.delete_node(3)
    l_list.traverse()
    l_list.insert_at_position(3, -2)
    l_list.traverse()
    l_list.update(3, -2)
    l_list.traverse()
    l_list.reverse()
    l_list.traverse()
