class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # return the length of the longest 
        # consecutive sequence of elemtns that can be formed


        # [1,4,5,2,6,4,6]
        d = set(nums)
        # remove duplicates
        res = 0

        for num in d:
            if num - 1 not in d:
                length = 1
                while num + length in d:
                    length += 1
                res = max(res, length) 
        return res
    
