class Solution:
    def trap(self, height: List[int]) -> int:
        
        left = 1
        right = len(height) - 2
        right_max = height[len(height) - 1]
        left_max = height[0]
        tot_water = 0

        while left <= right:

            if left_max < right_max:
                water = left_max - height[left]

                if height[left] > left_max:
                    left_max = height[left]

                left += 1
            
            else:
                water = right_max - height[right]

                if height[right] > right_max:
                    right_max = height[right]
                
                right -= 1
            
            if water > 0:
                tot_water += water

        return tot_water