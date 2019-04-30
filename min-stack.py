class MinStack: #intuitive

    def __init__(self):
        self.stack = []
    def push(self, x: int) -> None:
        self.stack.append(x)
    def pop(self) -> None:
        self.stack.pop()
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return min(self.stack)


class MinStack: #avoiding min()
    def __init__(self):
        self.stack = []

    def push(self, x):
        currentMin = self.getMin() #define currentMin
        if currentMin is None or x < currentMin: 
            currentMin = x #assign currentMin to x if it is the smallest element in stack
        self.stack.append((x, currentMin)) #second stack?
        return x

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return None if not self.stack else self.stack[-1][1]
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()