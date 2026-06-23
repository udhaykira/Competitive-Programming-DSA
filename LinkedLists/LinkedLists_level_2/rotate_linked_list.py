"""
LeetCode : 61 
Rotate List

Given the head of a linked list, rotate the list to the right by k places.

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:

Input: head = [0,1,2], k = 4
Output: [2,0,1]

"""
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        n = 0
        curr = head
        while curr:
            curr = curr.next
            n += 1

        k = k % n
        if k == 0:
            return head

        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy

        for i in range(k + 1):
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next

        new_head = slow.next
        slow.next = None
        
        curr = new_head
        while curr.next:
            curr = curr.next
        curr.next = dummy.next
        
        return new_head