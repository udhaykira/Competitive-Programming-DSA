"""
LeetCode : 73
Set Matrix Zeroes

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Example 1:

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r=len(matrix)
        c=len(matrix[0])
        fr = any(matrix[0][j]==0 for j in range(c))
        fc = any(matrix[i][0]==0 for i in range(r))

        for i in range(1,r):
            for j in range(1,c):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
            
        for i in range(1,r):
            for j in range(1,c):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        
        if fr:
            for j in range(c):
                matrix[0][j]=0
        
        if fc:
            for i in range(r):
                matrix[i][0]=0

        return matrix
            

        

        