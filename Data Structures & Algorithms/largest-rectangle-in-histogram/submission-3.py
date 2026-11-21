class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:


        max_rect = 0
        stack =[]

        for i in range(len(heights)):
            
            if heights[i] > max_rect:
                max_rect = heights[i]

            while stack and heights[i] < stack[-1][0]:
                    a = stack[-1][1]
                    area = stack[-1][0] * (i - a)
                    stack.pop()
                    if not stack or stack[-1][0] < heights[i]:
                        stack.append((heights[i], a))

                    if area > max_rect:
                        max_rect = area

            if stack and heights[i] > stack[-1][0]:
                    stack.append((heights[i], i))
            

            if not stack:
                stack.append((heights[i], i))




        for height,start in stack:

            area = height * (len(heights) - start)

            if area > max_rect:
                max_rect = area 

        return max_rect