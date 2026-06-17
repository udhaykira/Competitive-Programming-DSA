"""
Count Inversions in an Array

Given an integer array nums of size n, find the total number of inversions present in the array.

An inversion is a pair of indices (i, j) such that:

0 ≤ i < j < n
nums[i] > nums[j]

In other words, an inversion occurs when a larger element appears before a smaller element in the array.

Return the total number of inversions.

Example 1

Input:
nums = [2, 4, 1, 3, 5]
Output : 
3
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
            while j_count<len(right) and left[i_count]>right[j_count]:
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
            
    def countInversions(self, nums: list[int]) -> int:
        array, count = self.merge_sort(nums)
        return count