class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        dii1 = {}
        dii2 = {}

        for i in s1:
            dii1[i] = dii1.get(i , 0)+1
        
        current = 0
        
        while current < len(s1):
            dii2[s2[current]] = dii2.get(s2[current],0)+1
            current += 1
        
        right = current
        left = 0

        while right < len(s2):
            if dii1 == dii2:
                return True
            
            dii2[s2[right]] = dii2.get(s2[right],0)+1

            dii2[s2[left]] -= 1

            if dii2[s2[left]] == 0:
                del dii2[s2[left]]
            
            left += 1
            right += 1
        
        return dii1 == dii2
