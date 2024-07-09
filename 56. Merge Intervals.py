class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []

        # Sort intervals based on the starting point
        intervals.sort(key=lambda x: x[0])

        # List to hold the merged intervals
        merged = []

        # Initialize the first interval as the first interval in the sorted list
        merged.append(intervals[0])

        for i in range(1, len(intervals)):
            # Get the last merged interval
            last = merged[-1]

            # If the current interval overlaps with the last merged interval, merge them
            if intervals[i][0] <= last[1]:
                last[1] = max(last[1], intervals[i][1])
            else:
                # Otherwise, add the current interval to the merged intervals
                merged.append(intervals[i])

        return merged

        