"""
The Celebrity Problem

A celebrity is a person who is known to all but does not know anyone at a party. A party is being organized by some people. A square matrix mat[][] of size n*n is used to represent people at the party such that if an element of row i and column j is set to 1 it means ith person knows jth person. You need to return the index of the celebrity in the party, if the celebrity does not exist, return -1.

Note: Follow 0-based indexing.

Examples:

Input: mat[][] = [[1, 1, 0],
                [0, 1, 0],
                [0, 1, 1]]
Output: 1
Explanation: 0th and 2nd person both know 1st person and 1st person does not know anyone. Therefore, 1 is the celebrity person.

"""
class Solution:
    def celebrity(self, mat):
        # code here
        n = len(mat)
        stack = [i for i in range(n)]
        while len(stack)>1:
            p1 = stack.pop()
            p2 = stack.pop()
            
            if mat[p1][p2]==1:
                stack.append(p2)
            else:
                stack.append(p1)
        
        celebrity = stack.pop()
        for i in range(n):
            if i!=celebrity:
                if mat[celebrity][i]==1 or mat[i][celebrity]==0:
                    return -1
        return celebrity
        