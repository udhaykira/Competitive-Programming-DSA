"""
LeetCode : 560 
Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2

"""

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        d = {0:1}
        p = 0
        c=0
        for i in nums:
            p += i
            if p-k in d:
                c+=d[p-k]
            d[p] = d.get(p,0) + 1
        return c
        