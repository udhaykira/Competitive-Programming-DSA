"""
LeetCode : 725
Split Linked List in Parts

Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

Return an array of the k parts.

Example 1:

Input: head = [1,2,3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but its string representation as a ListNode is [].

"""
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> list[Optional[ListNode]]:
        curr = head
        n = 0

        while curr:
            curr = curr.next
            n+=1

        part = n//k
        extra = n%k

        curr = head
        result = []

        for i in range(k):
            part_head = curr
            size = part + (1 if i<extra else 0)

            for i in range(size-1):
                if curr:
                    curr = curr.next

            if curr:
                part_next = curr.next
                curr.next = None
                curr = part_next

            result.append(part_head)
            
        return result
                