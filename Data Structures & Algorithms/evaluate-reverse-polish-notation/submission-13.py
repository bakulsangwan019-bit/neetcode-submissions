class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        seen = {"+", "-", "*", "/"}

        stack = []

        for i in tokens:
            if i not in seen:
                stack.append(int(i))

            else:
                a = stack.pop()
                b = stack.pop()

                if i == "+":
                    current = b + a
                elif i == "-":
                    current = b - a
                elif i == "*":
                    current = b * a
                elif i == "/":
                    current = int(b / a)

                stack.append(current)
        
        return stack[0]