"""
LeetCode : 82
Remove Duplicates from Sorted List II

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

Example 1:

Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:

Input: head = [1,1,1,2,3]
Output: [2,3]

"""
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        curr = head
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        curr = head
        s = set()
        while curr and curr.next:
            if curr.val == curr.next.val:
                s.add(curr.val)
                prev.next = curr.next.next
            elif curr.val in s:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy.next
        
        