"""
LeetCode : 287
Find the Duplicate Number

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2

"""

class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        s = set()
        for i in nums:
            if i in s:
                return i
            else:
                s.add(i)
        
# Example usage:
solution = Solution()
nums = [1,3,4,2,2]
print(solution.findDuplicate(nums))  # Output: 2