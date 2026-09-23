class MinStack:

    def __init__(self):
        self.stac = []
        self.min_stack = []
        

    def push(self, val: int) -> None:

        self.stac.append(val)

        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        

    def pop(self) -> None:

        if self.stac.pop() == self.min_stack[-1]:
            self.min_stack.pop()
        

    def top(self) -> int:
        return self.stac[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        


stack = MinStack()