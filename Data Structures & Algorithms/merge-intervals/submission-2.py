class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 10/4 day 2 review

        # intervals is array of intervals, each: [start_i, end_i]
        # merge intervals when -> curr.start < prev.end
        # merge: merged list latest interval -> .end become max(merged.end, curr.end)
        # else: append to the merged list

        # 1. sort: sort by the first element, which is the start
        intervals.sort(key=lambda x: x[0])

        # initialize a merged list with the first element of the sorted intervals list
        merged = [intervals[0]]

        # loop through the list, merge if needed, otherwise -> append to the list
        for start, end in intervals[1:]:
            # if current start < merged[-1][1]: add to merge list
            if start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start,end])
        return merged
