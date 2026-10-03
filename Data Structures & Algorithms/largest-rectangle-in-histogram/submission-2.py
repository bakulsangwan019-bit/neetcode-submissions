class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0 

        for i in range(len(heights)):
            start = i

            while stack and heights[i] <= stack[-1][1]:

                a = stack.pop()

                width = i - a[0]
                area = a[1] * width

                if area > max_area:
                    max_area = area


                start = a[0]

            stack.append((start, heights[i]))

        for start, he in stack:
            width = len(heights) - start
            area = width * he

            if area > max_area:
                max_area = area
        
        return max_area


