#!/usr/bin/env python3

class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

stack1 = Stack()
print(stack1.data)
stack1.push(1)
print(stack1.data)
