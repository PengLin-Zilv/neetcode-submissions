class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # given list of nums
        # given target
        # return list of the 2 index of the two num add = target

        # we will have a dictionary for storing the num: its index
        # for each num, if their complement is in dict, we return
        # [key of complement, i] # smaller first

        # if not, we add it and its index into dict

        d = {}

        for i, n in enumerate(nums):
            complement = target - n
            if complement not in d:
                d[n] = i
            else:
                return [d[complement], i]
