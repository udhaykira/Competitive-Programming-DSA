"""
LeetCode : 143
Reorder List

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:

Input: head = [1,2,3,4]
Output: [1,4,2,3]

"""
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return
            
        nodes = []
        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next

        low, high = 0, len(nodes)-1

        while low<high:
            nodes[low].next = nodes[high]
            low += 1

            if low==high:
                break

            nodes[high].next = nodes[low]
            high-=1

        nodes[low].next = None
