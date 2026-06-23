"""
LeetCode : 160
Intersection of Two Linked Lists

Given the heads of two singly linked lists, return the node at which the two lists intersect. If the two linked lists have no intersection, return None.

"""
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA
        b = headB
        while a!=b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a
        