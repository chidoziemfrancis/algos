class Stack:
    def __init__(self):
        self.items = []

#four functions push, pop, peek and size
    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]

    def size(self):
        return len(self.items)

    def display(self):
        print(self.items)


# Example usage
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.display()
print(stack.pop())
print(stack.peek())
print(stack.size())
print(stack.is_empty())