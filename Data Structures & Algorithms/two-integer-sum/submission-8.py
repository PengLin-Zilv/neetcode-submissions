class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. Repeat the problem in own words
        # 2. State the approach with the time complexity
        # 3. Write clean code, talk while doing 

        # for a list of numbers, and an integer target
        # return two numbers' indices that add up to the target

        # use dictionary to store seen numbers and their indices, 
        # if match: add up to the target, return indices of them
        # so, return list of integer, with the smaller index first
        # return [seen[complement, i]

        # time complexity: O(n) since we loop through the list
        # space complexity will be O(n) since we storing the numbers and their index in a dictionary


        seen_dict = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in seen_dict:
                return [seen_dict[complement], i]
            seen_dict[n] = i


            
