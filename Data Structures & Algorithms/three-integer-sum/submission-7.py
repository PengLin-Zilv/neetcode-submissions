class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # we want to return a list of 3 nums that adds up to 0

        # for i in range(len(nums))
        # in addition to this, we will have l and r for the rigtside l and r movement
        # we will sort the list
        # num = [5,2,1,-5,3, -5,-3]
        # num.sort() = [-5, -5, -3,1,2,3,5]
        # loop from -5, check -3 to 5 if -5 + x + y = 0
        # -5 + 2 + 3

        # we also want to skip the duplicates, 

        result = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0: 
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])

                    l += 1
                    r -= 1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                    while l < r and nums[r+1] == nums[r]:
                        r -= 1

        return result
