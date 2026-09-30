class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # return the length of the longest 
        # consecutive sequence of elemtns that can be formed


        d = set()
        count = 0
        for n in nums:
            d.add(n)
        for n in nums:
            next_num = n + 1
            if next_num in d:
                count += 1
        return count