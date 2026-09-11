class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            store = []
            value = 1
            value2 = 1
            for i in range(len(nums)):
                if i != 0:
                    value *= nums[i-1]
                store.append(value)
            
            for j in range(len(nums)-1 , -1 , -1):
                if j != len(nums)-1:
                    value2 *= nums[j+1]
                store[j] *= value2
            
            return store