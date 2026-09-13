class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        store = []

        for i in range(len(nums)):
            a = i
            if i > 0 and nums[a] == nums[a-1]:
                continue
            
            left = i + 1
            right = len(nums) - 1

            while left < right:
                b = nums[left] + nums[right]
                
                if b > -nums[a]:
                    right -= 1
                
                elif b < -nums[a]:
                    left += 1
                
                else:
                    store.append([nums[a] , nums[left] , nums[right]])
                    
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                
        return store