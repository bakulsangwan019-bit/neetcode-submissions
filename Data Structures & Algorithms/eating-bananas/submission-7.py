class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        ans = None
        left = 1
        right = max(piles)

        while right >= left:
            mid = (left + right)//2

            hour = 0

            for i in piles:

                hour += math.ceil(i / mid)

            if hour > h:
                left = mid + 1

            else:
                ans = mid
                right = mid - 1
            
        return ans