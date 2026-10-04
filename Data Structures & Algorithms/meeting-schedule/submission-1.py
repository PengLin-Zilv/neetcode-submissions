"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # second day review (10/4/26)

        # array of meeting times given
        # with (start,end) each as interval

        # determine if a person could add all meetings to their schedule without conflict

        # False if -> curr.start > prev.end

        # 1. sort: sort intervals by start time
        intervals.sort(key=lambda x:x.start)

        # 2. loop and check conditions

        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False
        return True