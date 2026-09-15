class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        largest = 0

        for i in seen:
            countt = 1
            if i - 1 in seen:
                continue
            
            while i + 1 in seen:
                countt += 1
                i += 1
            
            if countt > largest:
                largest = countt
        
        return largest