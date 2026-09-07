class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        Input: String[] tokens
        Process: Evaluate the string in Reverse Polish Notation
        Output: Int answer

        ["1","2","+","3","*","4","-"]
        1 2 + == (1+2) == 3
        3 3 * == (3*3) == 9
        9 4 - == (9-4) == 5

        Brute force: iterate through but how to follow pemdas?
        Optimal: Use stack to keep rolling track of operations
        '''
        # Initiate stack
        stack = []
        # Initiate operations
        operations = {"+", "-", "*", "/"}
        # Iterate
        for token in tokens:
            # if operation
            if token in operations:
                # Pop twice
                rightNum = stack.pop()
                leftNum = stack.pop()
                # Handle each operation
                if token == "+":
                    solution =  leftNum + rightNum
                elif token == "-":
                    solution =  leftNum - rightNum
                elif token == "*":
                    solution = leftNum * rightNum
                else:
                    solution = int(leftNum / rightNum)
                # Push answer to stack
                stack.append(solution)
            # else
            else:
                # convert to int and push to stack
                stack.append(int(token))
        # Return stack[-1]
        return stack[-1]