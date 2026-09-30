class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums
        # target
        # return [i, j] which nums[i] + nums[j] == target

        d = {}
        # storing corresponding key and value for each num

        for i, n in enumerate(nums):
            # find the pair
            num2 = target - n
            if num2 in d:
                return [d[num2], i]
            else:
                d[n] = i