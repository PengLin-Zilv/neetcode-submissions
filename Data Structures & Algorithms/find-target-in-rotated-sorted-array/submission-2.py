class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # rotated list
        # one side must be clean
        # means: 1,2,3,...
        # or ...,3,4,5
        
        # so we check if target is within the clean sequence

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l+r)//2
            
            # 1. mid = target
            if nums[m] == target:
                return m
            
            # 2. left side is clean
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                    # we just search from l,...,r
                else: 
                    # go to right side
                    l = m + 1
            # 3. right side is clean
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1


            

