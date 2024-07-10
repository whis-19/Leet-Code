class Solution(object):
    def insert(self, intervals, newInterval):
        result = []
        i = 0
        n = len(intervals)

        # Step 1: Add all intervals ending before the new interval starts
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Step 2: Merge all overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # Step 3: Add the merged interval
        result.append(newInterval)

        # Step 4: Add all intervals starting after the new interval ends
        while i < n:
            result.append(intervals[i])
            i += 1

        return result
        