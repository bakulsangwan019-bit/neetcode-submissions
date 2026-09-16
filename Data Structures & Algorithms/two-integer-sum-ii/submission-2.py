class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        dii = {}
        index = 1

        for i in numbers:
            x = target - i
            if x not in dii:
                dii[i] = index
            else:
                return [dii[x] , index]
            
            index += 1
