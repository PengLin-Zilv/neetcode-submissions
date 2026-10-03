class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # base case: empty list -> []
        if not intervals:
            return []
        
        # SORT intervals by start
        intervals.sort(key=lambda x: x[0])
        # build the merged list with the first interval
        merged = [intervals[0]]

        # loop through the rest
        for start, end in intervals[1:]:
            # for each interval, [start, end]
            # intervals = [[1,2],[1,5],[3,6],[4,7]]
            # intervals[1:] = [[1,5], [3,6], [4,7]]

            # compare the next.start with prev.end
            # conditions:
            # 1. if overlap -> update the end with larger end time
            # 2. else -> directly append the interval
            if start <= merged[-1][1]:
                # overlap -> update the end
                merged[-1][1] = max(merged[-1][1], end)
            else:
                # not overlap
                merged.append([start,end])
        return merged




