class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         
         dii = {}
         index = 0

         for i in nums:
            x = target - i

            if x not in dii:
                dii[i] = index
            
            else:
                return[dii[x] , index]

            index += 1