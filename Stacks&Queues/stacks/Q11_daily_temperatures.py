"""
LeetCode : 739 
Daily Temperatures

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

"""
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        ans = [0]*n
        stack = []
        for i in range(n-1,-1,-1):
            while stack and stack[-1][0]<=temperatures[i]:
                stack.pop()
            
            if stack:
                ans[i]=stack[-1][-1] - i
            stack.append([temperatures[i],i])

        return ans
