class Solution:
    def isValid(self, s: str) -> bool:
        ans = False

        if len(s) != 0 and len(s)%2 == 0:       
            a = []
            ans = True
            dii = {")":"(", "]":"[", "}":"{"}

            for i in s:
                if i in dii:
                    if a and a[-1] == dii[i]:
                        a.pop()

                    else:
                        ans = False
                        break
                else:
                    a.append(i)
                    print(a)

            if len(a) != 0:
                ans = False

        return ans