class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # given an integer array nums, return an array output where output[i]
        # is the product of all elements except nums[i]
        
        # nums = [1,2,3,4]
        # if 1, we want 2 x 3 x 4
        # if 2, we want 1 x 3 x 4
        # all the left numbers times all the right side numbers
        
        res = []
        prod = 1

        # nums = [1,2,3,4]
        # 左边乘积
        for n in nums:
            res.append(prod)
            prod *= n
        # res = [1, 1, 2, 6]

        # 右边乘积
        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            # i in range(3,-1, -1)
            # 3,2,1,0
            res[i] *= prod
            prod *= nums[i]
        return res



