class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(i):
            if i >= len(nums):
                res.append(subset[:])
                return
            
            # Decision 1: take
            subset.append(nums[i])
            backtrack(i+1)
            subset.pop()

            # Decision 2: not take
            backtrack(i+1)

        backtrack(0)
        return res