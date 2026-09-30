class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right = len(nums)-1
        left = 0
        ans = -1

        while left <= right:
            mid = (left + right)//2

            if nums[mid] == target:
                ans = mid
                return ans
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return ans