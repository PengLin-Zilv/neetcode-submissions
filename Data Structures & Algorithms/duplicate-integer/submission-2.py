class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #brutal force 
        for i, num in enumerate(nums):
            if nums[i] == num:
                return True

        return False