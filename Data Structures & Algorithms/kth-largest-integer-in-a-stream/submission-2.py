import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # initializes the object given integer k and a stream of integer nums
        self.heap = []
        self.k = k
        
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        # adds the integer val, to the stream
        # returns the kth largest
        heapq.heappush(self.heap,val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
        
