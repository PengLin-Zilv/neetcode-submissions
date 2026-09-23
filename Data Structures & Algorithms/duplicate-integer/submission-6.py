class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # give nums, a list of integers
        # return true if anyvalue appears more than once

        seen = set()

        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False

