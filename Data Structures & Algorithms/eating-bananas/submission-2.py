class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = []

        while left <= right:
            mid = (left+right)//2
            total_hour = 0

            for pile in piles:
                total_hour += (pile + mid - 1) // mid

            if total_hour > h:
                left = mid + 1
            
            else:
                ans.append(mid)
                right = mid - 1
            
        return min(ans)