"""
You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2]. Each integer appears exactly once except a which appears twice and b which is missing. The task is to find the repeating and missing numbers a and b.

Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.

 

Example 1:

Input: grid = [[1,3],[2,2]]
Output: [2,4]
Explanation: Number 2 is repeated and number 4 is missing so the answer is [2,4].

"""
class Solution:
    def findMissingAndRepeatedValues(self, grid):
        n = len(grid)
        s = set()
        result = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] in s:
                    result.append(grid[i][j])
                else:
                    s.add(grid[i][j])
        for i in range(1,n*n + 1):
            if i not in s:
                result.append(i)
                break
        return result

# Example usage:
solution = Solution()
print(solution.findMissingAndRepeatedValues([[1,3],[2,2]]))  # Output: [2,4]

        