"""
LeetCode : 86
Partition List

Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:

Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

"""

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smaller = ListNode(0)
        greater = ListNode(0)

        small = smaller
        large = greater

        while head:
            if head.val<x:
                small.next = head
                small = small.next
            else:
                large.next = head
                large = large.next
            head = head.next
        
        large.next = None
        small.next = greater.next

        return smaller.next
        