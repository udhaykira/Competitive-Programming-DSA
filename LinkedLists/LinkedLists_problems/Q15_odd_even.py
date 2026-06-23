"""
LeetCode : 328
Odd Even Linked List

Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Example 1:

Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

"""
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        curr = head
        nodes = []
        while curr:
            nodes.append(curr)
            curr = curr.next
        odd_list = ListNode(0)
        even_list = ListNode(0)
        odd = odd_list
        even = even_list
        for i in range(len(nodes)):
            if i%2==0:
                odd.next = nodes[i]
                odd = odd.next
            else:
                even.next = nodes[i]
                even = even.next
            nodes[i].next = None
        odd.next = even_list.next
        return head