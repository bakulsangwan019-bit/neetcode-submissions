class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0 
        right = 0
        repeated = 0
        w_l = 0
        c_m = 0
        largest = 0
        dii = {}

        while right < len(s):
            dii[s[right]] = dii.get(s[right], 0) + 1
            w_l += 1
            c_m = max(dii.values())
            repeated = w_l - c_m
            right += 1
            

            while repeated > k:
                dii[s[left]] -= 1
                w_l -= 1
                c_m = max(dii.values())
                repeated = w_l - c_m
                left += 1
            
            if w_l > largest:
                largest = w_l
        
        return largest