"""

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

"""

class Solution:
    def majorityElement(self, nums):
        cand = None
        c = 0
        for i in range(len(nums)):
            if c==0:
                cand = nums[i]
                c = 1
            elif cand==nums[i]:
                c = c + 1
            else:
                c = c - 1
        return cand

# Example usage:
solution = Solution()
print(solution.majorityElement([3,2,3]))  # Output: 3
print(solution.majorityElement([2,2,1,1,1,2,2]))  # Output: 2
        