class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    # create a seen dictionary, document down the num and its position
        seen = {}

        for i, num in enumerate(nums):

            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
            # loop over nums
            # find the complement or add them to the dictionary
 