#!/usr/bin/env python3
""" Module to demonstrate a module using an array
"""
import sys


stack = []
stack_length = 10

def isEmpty():
    return True if len(stack) == 0 else False

def isFull():
    return True if len(stack) == 10 else False

def pop():
    if not isEmpty():
        element = stack.pop()
        return element
    else:
        print("Stack empty!")

def peek():
    if not isEmpty():
        element = stack[-1]
        return element
    else:
        print("Stack empty!")

def push(element):
    if not isFull():
        stack.append(element)
        return stack
    print("Stack full!")

def length():
    return len(stack)

if __name__ == "__main__":
    print("***Stack implementation using an array in Python***\n")
    print("Options\n")
    print("1.Check if stack is empty\n")
    print("2.Check if stack is full\n")
    print("3. Check and remove last element from stack\n")
    print("4. Check last element from stack\n")
    print("5. Add element to the stack\n")
    print("6. Check length of the stack\n")
    print("0. Exit the program")

    while True:
        option = input("Enter an option > ")
        if option == '1':
            print("Stack is empty\n") if isEmpty() else print("Stack isn't empty\n")
        elif option == '2':
            print("Stack is full\n") if isFull() else print("Stack isn't full\n")
        elif option == '3':
            print(f"Pop: {pop()}\n")
        elif option == '4':
            print(f"Peek: {peek()}\n")
        elif option == '5':
            element = input("Enter element to add to the stack > ")
            print(f"Stack: {push(element)}\n")
        elif option == '6':
            print(f"Lenght: {length()}\n")
        elif option == '0':
            sys.exit(0)
        else:
            print("Invalid option\n")
