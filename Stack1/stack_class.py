class Stack2:
    def __init__(self):
        self.top = -1
        self.s = list()

    def push(self, value):
        self.s.append(value)
        self.top += 1

    def pop(self):
        result = None
        if self.top > -1:
            result = self.s[self.top]
            self.s = self.s[:self.top]
            self.top -= 1
        return result

my_stack = Stack2()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())