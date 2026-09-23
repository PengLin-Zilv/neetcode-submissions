class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # so given list of heights
        # [1,3,5,7,4,6]
        # [7,2,1,4,6,8,8,1,9]
        # we wants to have the max Area
        # which = (r - l) x min(height[l],height[r])

        max_area = 0

        # we want to use two pointer to loop over the list to find the largest area
        # area function = (r - l) x min(height[l], height[r])

        l = 0
        r = len(heights) - 1

        while l < r:
            current_area = (r - l) * min(heights[l], heights[r])
            max_area = max(max_area, current_area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_area
