class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        n = len(nums)

        def backtrack(i):
            # base case
            if i == n:
                res.append(subset[:])
                return
            
            # first path: don't pick nums[i]
            backtrack(i+1)

            # second path: pick nums[i]
            subset.append(nums[i])
            backtrack(i+1)
            subset.pop()

        backtrack(0)
        return res
