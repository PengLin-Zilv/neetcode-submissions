class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # a list of nums
        # return the longest consecutive, length
        if not nums:
            return 0
        # sort the num
        nums.sort()
        count = 1
        # initialize the count
        res = 1
        # [2,3,5,6,8]
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] == nums[i-1] + 1:
                count += 1
                res = max(res, count)
            else:
                count = 1
        return res
