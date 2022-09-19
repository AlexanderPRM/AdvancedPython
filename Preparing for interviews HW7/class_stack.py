
class Stack:
    def __init__(self, stack: list):
        self.stack = stack

    def is_empty(self):
        return True if self.stack else False

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.is_empty():
            return self.stack.pop()
        else:
            print('Stack empty')

    def peek(self):
        if self.is_empty():
            return self.stack[-1]
        else:
            print('Stack empty')

    def size(self):
        return len(self.stack)

