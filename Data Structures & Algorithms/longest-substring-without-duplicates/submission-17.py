class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dii = {}
        left = 0
        right = 0
        max_len = 0
        repeated = 0
        w_l = 0

        while right <= len(s)-1:
            
            if repeated == 0:
                dii[s[right]] = dii.get(s[right],0) + 1
                w_l += 1
                curr = len(dii)
                repeated = w_l - curr

                if curr > max_len:
                    max_len = curr
                right += 1

            elif repeated > 0:
                dii[s[left]] -= 1

                if dii[s[left]] == 0:
                    del dii[s[left]]
                w_l -= 1
                curr = len(dii)
                repeated = w_l - curr
                left += 1
        
        return max_len
