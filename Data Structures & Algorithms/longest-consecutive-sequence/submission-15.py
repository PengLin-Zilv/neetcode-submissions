class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # giving array of integers nums
        # return the length of the longest consecutive sequence
        # first we use set(), O(1) look up

        # loop through nums - O(n)

        # for each n: while last number exist, n - 1
        # count += 1
        # update max_count

        # what we counting, initialize a count variable
        
        count = 0
        max_count = 0

        sorted_nums = set(nums)

        # for each num in nums:
        for num in sorted_nums:
            if num - 1 not in sorted_nums:
                count = 1
                current = num
                while current + 1 in sorted_nums:
                    current += 1
                    count += 1
            
                max_count = max(max_count, count)
        return max_count