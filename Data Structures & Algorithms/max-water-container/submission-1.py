class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # the formula for water area
        # width = r - l
        # height = min(heights[l], heights[r])
        # Area = w * h

        # key point, we use two pointer to keep compressing

        l = 0
        r = len(heights) - 1

        max_area = 0

        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            current_area = width * height

            max_area = max(max_area, current_area)

            if heights[l] < heights[r]:
                l += 1
            else: 
                r -= 1
                

        return max_area