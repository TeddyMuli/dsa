#!/usr/bin/env python3
""" Python module to demonstrate a singly linked list
"""


class Node():
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

def insert_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def traverse(head):
    current = head
    while current:
        print(str(current.data) + "->", end=" ")
        current = current.next

    print("None")

def reverse(head):
    current = head
    previous = None
    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous

def delete_node(head, key):
    current = head
    previous = None

    # If head node itself holds the key to be deleted
    if current is not None:
        if current.data == key:
            head = current.next
            current = None
            return head

    # Search for the key to be deleted, keep track of the previous node
    while current is not None:
        if current.data == key:
            break
        previous = current
        current = current.next

    # If key was not present in linked list
    if current == None:
        return head

    # Unlink the node from linked list
    previous.next = current.next
    current = None

    return head

head = None
head = insert_beginning(head, "d")
head = insert_beginning(head, "c")
head = insert_beginning(head, "b")
head = insert_beginning(head, "a")

traverse(head)
head = reverse(head)
traverse(head)
head = delete_node(head, "c")
traverse(head)
