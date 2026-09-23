class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # three sum
        # give a list of nums
        # return all the triples [[a,b,c], [x,y,z]]
        # that adds up to 0 and i,j,l are distinct
        
        # we want to loop over the nums,
        # ex: [-1,0,1,2,-1,-4]
        # return list of lists of integers

        result = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            r = len(nums) - 1
            while j < r:
                # moving j to the right, r to the left
                # while checking if requirement meet
                total = nums[i] + nums[j] + nums[r]
                if total < 0:
                    j += 1
                elif total > 0:
                    r -= 1
                else:
                    result.append([nums[i], nums[j], nums[r]])

                    j += 1
                    r -= 1
                    while j < r and nums[j] == nums[j-1]:
                        j += 1
                    while j < r and nums[r] == nums[r+1]:
                        r -= 1
        return result

