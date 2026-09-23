class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # list of nums = [3,4,5,7]
        # a target
        # return a list of indexes of the nums that adds up to the target
        # if target = 7, nums will be 3 and 4
        # and result will be [1,2]  their index
        # first: use dictionary

        d = {}

        for i, n in enumerate(nums):
            complement = target - n
            # so if 0,3. Target = 7, complement = 4
            if complement not in d:
                d[n] = i
            # so d = {3:0, 4:1}
            else:
            # lets say it is 1,4. complement = 3
                return [d[complement], i]