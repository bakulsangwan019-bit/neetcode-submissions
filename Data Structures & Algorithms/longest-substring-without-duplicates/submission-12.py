class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0

        tot = 0
        large = 0
        left = 0
        right = 0
        seen = set()

        while right < len(s):

            if s[right] not in seen:
                seen.add(s[right])
                tot += 1

                if tot > large:
                    large = tot

                right += 1

            else:
                seen.remove(s[left])
                tot -= 1
                left += 1

        return large