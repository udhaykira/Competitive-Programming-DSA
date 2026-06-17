"""
LeetCode : 493
Reverse Pairs

Given an integer array nums, return the number of reverse pairs in the array.

A reverse pair is a pair (i, j) where:

0 <= i < j < nums.length and
nums[i] > 2 * nums[j].
 
Example 1:

Input: nums = [1,3,2,3,1]
Output: 2
Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1

"""

class Solution:
    def merge_sort(self, nums):
        if len(nums)<=1:
            return nums,0
        mid = len(nums)//2
        left, left_idx = self.merge_sort(nums[:mid])
        right, right_idx = self.merge_sort(nums[mid:])

        i=j=0
        result = []
        c = left_idx + right_idx
        j_count = 0
        for i_count in range(len(left)):
            while j_count<len(right) and left[i_count]>2*right[j_count]:
                j_count+=1
            c+=j_count


        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
            
        while i<len(left):
            result.append(left[i])
            i+=1
        while j<len(right):
            result.append(right[j])
            j+=1
        return result, c
            
    def reversePairs(self, nums: list[int]) -> int:
        array, count = self.merge_sort(nums)
        return count