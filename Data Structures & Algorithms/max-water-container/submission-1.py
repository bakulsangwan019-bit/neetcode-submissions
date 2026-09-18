class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        largest = 0

        while left < right:
            height = min(heights[right] , heights[left])
            width = right - left
            area = height * width

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
            
            if largest < area:
                largest = area
        
        return largest
