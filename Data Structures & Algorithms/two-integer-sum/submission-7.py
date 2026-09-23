class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums: list of integers, and a target which is an integer
        # return the indices of the two integers that adds up to target

        d = {} # an empty dictionary storing num: its index
        for i, n in enumerate(nums):
            complement = target - n
        # nums = [1,2,3,4]
        # target = 4
        # for n = 1, complement = 3

            if complement in d:
                return [d[complement], i]
            d[n] = i
