class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        largest = 0

        while left < right:
            height = min(heights[left] , heights[right])
            width = right - left
            area = height * width

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            if area > largest:
                largest = area
        
        return largest
