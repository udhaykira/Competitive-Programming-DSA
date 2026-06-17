"""
LeetCode : 84
Largest Rectangle in Histogram

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

"""

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        n = len(heights)
        max_area = 0

        for i in range(n+1):
            curr = 0 if i==n else heights[i]

            while stack and heights[stack[-1]]>curr:
                h = heights[stack.pop()]

                if stack:
                    w = i - stack[-1] - 1
                else:
                    w = i
                max_area = max(max_area, h * w)
                
            stack.append(i)

        return max_area
        