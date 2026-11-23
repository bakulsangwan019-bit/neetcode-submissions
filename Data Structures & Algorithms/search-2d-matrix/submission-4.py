class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        left = 0 
        r = len(matrix)
        c = len(matrix[0])

        right = r * c - 1
        ans = False

        while right >= left:

            mid = (right+left)//2
            row = mid // c
            col = mid % c

            if matrix[row][col] == target:
                ans = True
                return ans
            
            elif matrix[row][col] < target:
                left = mid + 1

            else:
                right = mid - 1

        return ans
