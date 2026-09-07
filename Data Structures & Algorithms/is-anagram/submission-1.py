class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dii1 = {}
        dii2 = {}

        for i in s:
            dii1.setdefault(i,0)
            dii1[i] += 1

        for j in t:
            dii2.setdefault(j,0)
            dii2[j] += 1

        for k in dii1:
            if k not in dii2 or dii1[k] != dii2[k]:
                return False

        return True