"""
LeetCode : 1019
Next Greater Node In Linked List

You are given the head of a linked list with n nodes.

For each node in the list, find the value of the next greater node. That is, for each node, find the value of the first node that is next to it and has a strictly larger value than it.

Return an integer array answer where answer[i] is the value of the next greater node of the ith node (1-indexed). If the ith node does not have a next greater node, set answer[i] = 0.

Example 1:

Input: head = [2,1,5]
Output: [5,5,0]

"""
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> list[int]:
        if not head:
            return []
        stack = []
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        curr = prev
        result = []
        while curr:
            while stack and stack[-1]<=curr.val:
                stack.pop()
            if stack:
                result.append(stack[-1])
            else:
                result.append(0)
            stack.append(curr.val)
            curr = curr.next
        result = result[::-1]
        return result
        

        