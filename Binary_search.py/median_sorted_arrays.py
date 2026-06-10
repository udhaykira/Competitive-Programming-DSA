"""
LeetCode : 4
Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        arr = [0] * (m + n)
        k = m + n - 1

        i = m - 1
        j = n - 1

        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                arr[k] = nums1[i]
                i -= 1
            else:
                arr[k] = nums2[j]
                j -= 1
            k -= 1

        while i >= 0:
            arr[k] = nums1[i]
            i -= 1
            k -= 1

        while j >= 0:
            arr[k] = nums2[j]
            j -= 1
            k -= 1

        length = len(arr)

        if length % 2 == 1:
            return arr[length // 2]
        else:
            return (arr[length // 2] + arr[length // 2 - 1]) / 2