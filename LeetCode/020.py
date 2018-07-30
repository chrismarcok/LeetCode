def isValid(s):
    """
    >>> isValid("()")
    True
    >>> isValid("()[]{}")
    True
    >>> isValid("(}")
    False
    >>> isValid("([)]")
    False
    >>> isValid("{()}")
    True
    >>> isValid("[")
    False
    """

    stack = Stack()

    for x in s:
        if x == '(' or x == '[' or x == '{':
            stack.push(x)
        else:
            if x == ')':
                if stack.pop() == '(':
                    continue
                else:
                    return False
            if x == '}':
                if stack.pop() == '{':
                    continue
                else:
                    return False
            if x == ']':
                if stack.pop() == '[':
                    continue
                else:
                    return False
    return stack.isEmpty()


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return "POOP"
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)
