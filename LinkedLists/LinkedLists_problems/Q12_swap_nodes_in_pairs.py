"""
LeetCode : 24 
Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.) 

Example 1:

Input: head = [1,2,3,4]
Output: [2,1,4,3]

"""
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
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
        while n >= 2:
            group_tail = curr 
            prev = None
            
            for _ in range(2):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                
            group_prev.next = prev 
            group_tail.next = curr 
            group_prev = group_tail
            n -= 2
            
        return dummy.next