"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

"""

class Solution:
    def spiralOrder(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        res = []
        top, bottom, left, right = 0, m, 0, n
        while top<bottom and left<right:
            for i in range(left,right):
                res.append(matrix[top][i])
            top+=1

            for i in range(top,bottom):
                res.append(matrix[i][right-1])
            right-=1

            if top<bottom:
                for i in range(right-1,left-1,-1):
                    res.append(matrix[bottom-1][i])
                bottom-=1
                
            if left<right:
                for i in range(bottom-1,top-1,-1):
                    res.append(matrix[i][left])
                left+=1
        return res

# Example usage:
solution = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(solution.spiralOrder(matrix))  # Output: [1,2,3,6,9,8,7,4,5]