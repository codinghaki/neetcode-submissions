class MinStack:
    '''
    Stack: [0,-1,2,3]
    Minstack: [0,-1,-1,-1]
    '''

    def __init__(self):
        # Stack
        self.stack = []
        # Minstack
        self.minStack = []

    def push(self, val: int) -> None:
        # Push to stack
        self.stack.append(val)
        # If val < minstack[-1] push val to minstack else minstack[-1]
        if not self.minStack:
            self.minStack.append(val)
            return

        if val < self.minStack[-1]:
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1])

    def pop(self) -> None:
        # Pop stack
        self.stack.pop()
        # Pop minstack
        self.minStack.pop()

    def top(self) -> int:
        # Return stack[-1]
        return self.stack[-1]

    def getMin(self) -> int:
        # Return minstack[-1]
        return self.minStack[-1]