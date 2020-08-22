# Given a collection of intervals, merge all overlapping intervals.

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# Note: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

 

# Constraints:

# intervals[i][0] <= intervals[i][1]


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # return [[1,6],[8,10],[15,18]]
        
        if not intervals:
            return intervals
        intervals.sort(key=lambda x:x[0])
        
        m = []
        
        for inter in intervals:
#             condition for appending in to array
            if not m or m[-1][1] < inter[0]:
                m.append(inter)
            else:
                m[-1][1] = max(m[-1][1],inter[1])
        return m
        
        
        
        