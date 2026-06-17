"""
LeetCode : 240
Search a 2D Matrix ||

Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Example 1:

Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true

"""

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        r,c = 0, len(matrix[0])-1
        while r<len(matrix) and c>=0:
            if matrix[r][c]==target:
                return True
            elif matrix[r][c]<target:
                r+=1
            else:
               c-=1
        return False
