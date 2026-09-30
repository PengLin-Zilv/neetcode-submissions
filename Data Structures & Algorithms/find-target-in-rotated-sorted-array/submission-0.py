class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # given rotated sorted array
        # given target
        # return nums[target]

        # [3,4,5,6,1,2], target = 6
        # return 4

        for n in nums:
            if n == target:
                return nums[n]
        else:
            return -1
