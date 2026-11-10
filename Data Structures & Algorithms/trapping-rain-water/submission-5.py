class Solution:
    def trap(self, height: List[int]) -> int:
        
        tot_water = 0

        if height:
            left = 0
            right = len(height) - 1

            left_max = height[left]
            right_max = height[right]




            while left < right:
                if height[left] <= height[right]:
                    left += 1
                    
                    if height[left] >= left_max:
                        left_max = height[left]


                    else:
                        water = left_max - height[left]
                        tot_water += water


                else:

                    right -= 1

                    if height[right] >= right_max:
                        right_max = height[right]

                    
                    else:
                        water = right_max - height[right]
                        tot_water += water
                
            return tot_water