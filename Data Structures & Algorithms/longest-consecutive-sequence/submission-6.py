class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # longest consecutive
        # use hash map
        if not nums:
            return 0

        count = 0 
        nums = sorted(set(nums))
        longest = current = 1
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
            # if the current num is next nums + 1
                current += 1
                longest = max(current, longest)
            else:
                current = 1
        return longest

        # 2,3,4,5,9,10
        # n = 2, j will be: 2,3,4,5,9,10, for len(n) times
        # if j = n-1
        # for n = 2, there is none

        # for n = 10,