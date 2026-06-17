"""
LeetCode : 50
Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100

"""
class Solution:
    def helper(self,x,n):
        if n==0:
            return 1
        temp = self.helper(x,n//2)
        temp = temp*temp
        if n%2!=0:
            temp*=x
        return temp

    def myPow(self, x: float, n: int) -> float:
        if n<0:
            n=-n
            return 1/self.helper(x,n)
        return self.helper(x,n)
        

# Example usage:
solution = Solution()
print(solution.myPow(2.00000, 10))  # Output: 1024.00000
print(solution.myPow(2.10000, 3))   # Output: 9