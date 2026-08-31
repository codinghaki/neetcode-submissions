class Solution:
    def isValid(self, s: str) -> bool:
        """
        Input: string s
            Consists of: [(,),{,},[,]]
        Task: Check if s is valid
            - Every open bracket is closed by same type
            - Open brackets are closed in correct order
            - Every close bracket has corresponding of same type
        Output: True if valid else False

        Eg1 "[]" true
        Eg2 "([{}])" true
        Eg3 "[(])" false, ( needs to be closed before ] comes
        Eg4 "()()()" true

        Brute force: For every open bracket check next closing is correct
        """
        # Maintain brackets
        brackets = {
            "(":")",
            "{":"}",
            "[":"]"
        }
        # Maintain stack
        stack = []
        # Iterate through string
        for bracket in s:
            # If open bracket then push corresponding closing
            if bracket in brackets:
                stack.append(brackets[bracket])
            elif not stack:
                return False
            # If closing bracket then pop from stack and check theyre same
            else:
                topBracket = stack.pop()
                if topBracket != bracket:
                    return False
        # If stack not empty by end of loop means invalid
        if stack:
            return False 
        else:
            return True