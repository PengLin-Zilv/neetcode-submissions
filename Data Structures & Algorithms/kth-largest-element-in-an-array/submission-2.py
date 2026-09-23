import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # given k and nums, find k largest num in nums
        # initialize a heap
        heap = []

        for n in nums:
            heapq.heappush(heap, n)

            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
            