class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack =[]
        area = 0

        for i in range(n + 1):
            while stack and (i == n or heights[stack[-1]] >= heights[i]):
                height = heights[stack.pop()]
                wid = i if not stack else (i - stack[-1] - 1)
                area = max(area, height * wid)
            stack.append(i)
        return area