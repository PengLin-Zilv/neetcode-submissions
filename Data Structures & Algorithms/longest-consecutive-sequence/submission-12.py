class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # given nums, list
        # we want longest consecutive count
        # sort the nums

        if not nums:
            return 0

        sorted_list = sorted(set(nums))
        count = 1
        res = 1

        # nums = [1,1,2,3,6,7,8]
        for i in range(1, len(sorted_list)):
            if sorted_list[i] == sorted_list[i-1] +1:
                count += 1
                res = max(res, count)
            else:
                count = 1
        return res