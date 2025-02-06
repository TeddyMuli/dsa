#!/usr/bin/env python3
''' Python module for double linked lists
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

