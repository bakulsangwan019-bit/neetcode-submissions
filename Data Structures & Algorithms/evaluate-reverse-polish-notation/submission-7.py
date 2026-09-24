import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        seen = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda b, a: int(b / a)
        }
        
        stack = []
        
        for i in tokens:
            if i not in seen:
                stack.append(int(i))
            else:
                a = stack.pop()
                b = stack.pop()
                
                current = seen[i](b, a)
                stack.append(current)
                

        return stack[0]