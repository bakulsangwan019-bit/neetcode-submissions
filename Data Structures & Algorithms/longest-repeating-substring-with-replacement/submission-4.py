class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0 
        right = 0
        w_l = 0
        dii = {}
        largest = 0

        while right < len(s):
            dii[s[right]] = dii.get(s[right],0) + 1
            w_l += 1
            max_curr = max(dii.values())
            curr = w_l - max_curr
            right += 1

            while curr > k:
                dii[s[left]] -= 1

                if dii[s[left]] == 0:
                    del dii[s[left]]

                w_l -= 1
                max_curr = max(dii.values())
                curr = w_l - max_curr
                left += 1

            if w_l > largest:
                largest = w_l
        
        return largest
        