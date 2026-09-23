class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        # this makes the count dictionary
        arr = []
        # {3:2, 4:1, 5:3}
        for num, cnt in count.items():
            arr.append([cnt,num])
        arr.sort()
        # arr = [[3,2], [2,2], [4,3]]
        # arr.sort() = [[2,2], [3,2], [4,3]]
        
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res


        # Time Complexity: O(n log n), the sorting part is slowest
        # Space Complexity: O(n)  actually is O(n+n+k)

