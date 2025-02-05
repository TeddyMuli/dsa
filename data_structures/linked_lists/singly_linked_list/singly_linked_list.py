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
        new_node = Node(data)
        current = self.head
        self.head = new_node
        new_node.next = current

    def insert_at_end(self, data):
        new_node = Node(data)
        current = self.head
        while current:
            if current.next == None:
                current.next = new_node
                break

            current = current.next


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
