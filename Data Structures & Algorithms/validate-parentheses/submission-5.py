class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        dii = {"}":"{", ")":"(", "]":"["}

        stack = []
        for i in s:
            if i in dii.values():
                stack.append(i)

            elif i in dii:
                if not stack or dii[i] != stack[-1]:
                    return False
                stack.pop()
            else:
                return False
        
        return len(stack) == 0