import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # stones, stone[i] is weight of ith stone

        # in each step, we choose heaviest
        # smash
        # if x == y, both gone
        # if x < y, x is gone
        # y = y - x
        # return the weight of the last stone, or 0 if none remain

        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            # first two
            # if x == y, gone
            # if x < y, x is gone
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            # if x > y, x become x-y
            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])