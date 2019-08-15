class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        length = 0
        temp = []
        while (len(self.stack) is not 0):
            temp.append(self.stack.pop(0))
            length += 1
        
        for x in range(length - 1):
            self.stack.append(temp.pop(0))
            
        result = temp.pop(0)
        return result
    
    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        length = 0
        temp = []
        while (len(self.stack) is not 0):
            temp.append(self.stack.pop(0))
            length += 1
        
        for x in range(length - 1):
            self.stack.append(temp.pop(0))
            
        result = temp.pop(0)
        self.stack.append(result)
        return result

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.stack) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()