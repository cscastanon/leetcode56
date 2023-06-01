#Leetcode 56
# Runtime: O(nlogn) where n = the # of elements(intervals)
# Space complexity: O(n), where n = # of elements in result array

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i:i[0])
        result = [intervals[0]]
        for x,y in intervals[1:]:
            lastEnd = result[-1][1]
            if x <= lastEnd:    #overlap case
                result[-1][1] = max([y, lastEnd])
            else:       #no overlapping case
                result.append([x,y])
        return result