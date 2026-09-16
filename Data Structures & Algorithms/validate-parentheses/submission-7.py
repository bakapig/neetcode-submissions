class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }


        for char in s:
            # Opening bracket
            if char in '([{':
                stack.append(char)
            # Closing bracket
            else:
                if len(stack) == 0:
                    return False
                if stack[-1] != pairs[char]:
                    return False

                stack.pop()

        if len(stack) == 0:
            return True
        else:
            return False

        