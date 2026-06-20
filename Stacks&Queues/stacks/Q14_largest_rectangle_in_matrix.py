"""
LeetCode : 85
Maximal Rectangle

Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example 1:

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.

"""

class Solution:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0

        cols = len(matrix[0])
        heights = [0] * cols
        ans = 0

        for row in matrix:

            for j in range(cols):
                if row[j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0

            stack = []

            for i in range(cols + 1):
                curr = 0 if i == cols else heights[i]

                while stack and heights[stack[-1]] > curr:
                    h = heights[stack.pop()]

                    if stack:
                        w = i - stack[-1] - 1
                    else:
                        w = i

                    ans = max(ans, h * w)

                stack.append(i)

        return ans