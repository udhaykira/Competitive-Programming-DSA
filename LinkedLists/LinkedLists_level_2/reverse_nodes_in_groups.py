"""
LeetCode : 25
Reverse Nodes in k-Group

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

"""
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
            
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        
        curr = head
        while n >= k:
            group_tail = curr 
            prev = None
            
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                
            group_prev.next = prev 
            group_tail.next = curr 
            group_prev = group_tail
            n -= k
            
        return dummy.next