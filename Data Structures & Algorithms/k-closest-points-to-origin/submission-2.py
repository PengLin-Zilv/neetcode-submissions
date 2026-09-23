import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # given 2D array points
        # points[i] = [xi, yi]
        # given k
        # return k closest points to origin 

        # formula for distance is sqrt((x1 - x2)^2 + (y1 - y2)^2))
        max_q = [] 
        for x, y in points:
            distance = x*x + y*y
            heapq.heappush(max_q, (-distance, x, y))
            if len(max_q) > k:
                heapq.heappop(max_q)
        
        result = []
        for item in max_q:
            result.append([item[1], item[2]])
        return result
