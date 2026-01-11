from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # Step 1: sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]

        # Step 2: merge overlapping intervals
        for start, end in intervals[1:]:
            last_end = merged[-1][1]

            if start <= last_end:  # overlapping or touching
                merged[-1][1] = max(last_end, end)
            else:
                merged.append([start, end])

        return merged
