class MinStack:

    def __init__(self):

        self.st=[]

        
        

    def push(self, x: int) -> None:

        min_so_far = x if not self.st else min(self.st[-1][1], x)
        self.st.append((x, min_so_far))
        

    def pop(self) -> None:

        self.st.pop()
        

    def top(self) -> int:

        return self.st[-1][0]
        

    def getMin(self) -> int:

        return self.st[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()