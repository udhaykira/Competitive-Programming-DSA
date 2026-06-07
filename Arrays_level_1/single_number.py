"""
LeetCode : 136
Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:

Input: nums = [2,2,1]

Output: 1
"""

class Solution:
    def singleNumber(self, nums):
        d = nums[0]
        for i in nums[1:]:
            d = d ^ i
        return d

# Example usage:
solution = Solution()
print(solution.singleNumber([2,2,1]))  # Output: 1
        