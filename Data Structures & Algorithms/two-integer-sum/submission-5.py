class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        # empty dictionary to store the num and value
        # this problem asking for the two indices, the num's value that adds up to the target

        for i, num in enumerate(nums):
            difference = target - num
            if difference in d:
                return [d[difference], i]
            d[num] = i

        # target = 7
        # nums = [3,4,5,6]
        # return [0,1] because they're the indices of 3 and 4 which adds up to 7, the target

        # d = {3:0}
        # num now is 4

        

        # first num = 3, difference not in d
        # d.append

