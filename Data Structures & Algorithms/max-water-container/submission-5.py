class Solution:
    def maxArea(self, heights: List[int]) -> int:

        ans = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            width = right - left 
            hei = min(heights[left] , heights[right])

            area = width * hei

            if hei == heights[left]:
                left += 1
            else:
                right -= 1

            if ans < area:
                ans = area

        return ans
        