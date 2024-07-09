class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        brackets = {
        ")": "(",
        "}": "{",
        "]": "["
        }
        stack = []

        for char in s:
            if char in brackets:  
                if not stack or stack.pop() != brackets[char]:
                    return False
            else:
                stack.append(char)

        return not stack