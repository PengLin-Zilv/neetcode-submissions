class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # given an integer array nums
        # return true if n appears >1 times

        seen = set()

        for n in nums:
            if n in seen:
                return Ture
        return False