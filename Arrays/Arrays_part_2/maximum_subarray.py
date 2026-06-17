"""
LeetCode : 53 
Maximum Subarray & Kadane Algorithm

Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

"""

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        curr_sum = max_sum = nums[0]
        for i in range(1,len(nums)):
            curr_sum = max(nums[i],curr_sum + nums[i])
            max_sum = max(max_sum,curr_sum)
        return max_sum

# Example usage:
solution = Solution()
print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6
print(solution.maxSubArray([1]))  # Output: 1

        