class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dii = {}
        dii1 = {}

        for i in t:
            dii[i] = dii.get(i,0)+1

        left = 0
        right = 0
        a = False
        w_l = float("inf")
        best_wind = ""

        while right < len(s):
            dii1[s[right]] = dii1.get(s[right], 0) +1

            right += 1


            for i in dii:

                if i not in dii1 or dii1[i] < dii[i]:  
                    a = False
                    break
            else:
                a = True

            while a == True:
                if (right- left) < w_l:
                    w_l = right - left
                    best_wind = s[left:right]

                dii1[s[left]] -= 1
                if dii1[s[left]] == 0:
                    del dii1[s[left]]
            

                if s[left] in dii and dii1.get(s[left], 0) < dii[s[left]]:
                    a = False
                left += 1
        return best_wind