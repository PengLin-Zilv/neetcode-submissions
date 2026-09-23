class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # question asking to return an int
        # counting how long is the consecutive list
        # for example
        # [2,4,10,9,3,5]
        # [2,3,4,5] count = 4
        # return 4

        # 1. we need to sort this so it become [2,3,4,5,9,10]
        # 2. we need a count
        if not nums:
            return 0
        count = 1
        sorted_list = sorted(set(nums))
        length = 1

        for i in range(1, len(sorted_list)):
            if sorted_list[i] == sorted_list[i-1] + 1:
                count += 1
                length = max(count, length)
            else: 
                count = 1
        return length

