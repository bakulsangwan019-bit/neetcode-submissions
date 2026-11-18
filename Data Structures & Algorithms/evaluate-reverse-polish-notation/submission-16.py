class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = None
        ope = ["+","/","*","-"]

        for i in tokens:
            if i not in ope:
                stack.append(i)

            if i in ope:
                a = int(stack.pop())
                b = int(stack.pop())

                if i == "+":
                    result = b + a
                elif i == "*":
                    result = b * a
                elif i == "-":
                    result = b - a
                else:
                    if a != 0:
                        result = int(b/a)
                    else:
                        print("Invalid")

                stack.append(result)
        
        return int(stack[-1])