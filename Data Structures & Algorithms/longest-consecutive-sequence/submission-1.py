class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # return the length of the longest 
        # consecutive sequence of elemtns that can be formed


        d = set(nums)
        count = 0
        for n in nums:
            if n - 1 not in d:
                length = 1
                while n + length in d:
                    length += 1
                count = max(count, length)
        return count
