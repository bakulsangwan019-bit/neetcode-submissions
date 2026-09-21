class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current = 0
        seen = set()
        for i in range(len(s)):
            if s[i] in seen:
                break

            current += 1
            seen.add(s[i])
        
        left = 0
        right = current
        largest = current

        while right < len(s):
            if s[right] in seen:
                seen.remove(s[left])
                left += 1
                current -= 1
            else:
                seen.add(s[right])
                right += 1
                current += 1
            
            if current > largest:
                largest = current 
        
        return largest