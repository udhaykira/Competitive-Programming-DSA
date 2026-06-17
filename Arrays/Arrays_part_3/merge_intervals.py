"""
LeetCode : 56
Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

"""

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        x=[]
        comp=intervals[0]
        for i in range(1,len(intervals)):
            if comp[1]>=intervals[i][0]:
                comp[1]=max(comp[1],intervals[i][1])
            else:
                x.append(comp)
                comp=intervals[i]
        x.append(comp)
        return x

        