"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # if not intervals:
        #     return 0

        # intervals.sort(key=lambda x: x[0])

        # min_heap = []

        # for start, end in intervals:

        #     if min_heap and min_heap[0] <= start:
        #         heapq.heappush(min_heap)

        #     heapq.heappush(min_heap, end)

        # return (len(min_heap))
        intervals.sort(key=lambda x: x.start)
        min_heap = []

        for interval in intervals:
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval.end)

        return len(min_heap)
