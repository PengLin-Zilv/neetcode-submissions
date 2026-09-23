class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            medium = (l + r) // 2
            # [1,2,3,4,5]
            # [5,1,2,3,4]
            # [2,3,4,5,1]
            if nums[medium] < nums[r]:
                r = medium
            else:
                l = medium + 1
        return nums[l]
            

