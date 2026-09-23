class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # we want return a list of [x,y,z] which x + y + z = 0
        # we want to loop over the list, 
        # for i in range(len(nums))
        # and use two pointers

        # we also want to set result list
        result = []

        # sort the nums list
        nums.sort()  # this takes O(n lgn n) time


        # same things for two pointers,
        # for each i
        # we move l and r
        # we also skip duplicates
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1

            if i > 0 and nums[i] == nums[i-1]:
                continue

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

                    while l < r and nums[l] == nums[l-1]:
                            l += 1
                    while l < r and nums[r] == nums[r+1]:
                            r -= 1
        return result
                        