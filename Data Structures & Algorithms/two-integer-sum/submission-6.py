class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # have a target
        # have a list of nums
        # return the index of two numbers that adds to target

        # we will use dictionary, store existing numbers
        # let's say the nums = [1,3,2,4]
        # target = 5

        # lets say we have 1, we want to find a 4 to reach the target
        # So we will also have an element called complement

        # for i, n in enumerate(nums):
        # i = 0, n = 1
        # i = 1, n = 3


        # empty dic to store the values

        d = {} # store {number: its index}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in d:
                return [d[complement], i]
            else:
                d[num] = i





