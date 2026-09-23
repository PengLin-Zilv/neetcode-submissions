class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a empty dictionary
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num
            # target = 7
            # complement = target - 3 = 4

            # we need the index of 3 and 4
            # if we have, return index of num and, i
            # if we don't, add the number to dictionary

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i
        return {}
 