"""
LeetCode : 142
Linked List Cycle II

Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break

        if not fast or not fast.next:
            return None
        slow = head
        while slow!=fast:
            slow = slow.next
            fast = fast.next

            if slow == fast:
                break
        return slow
        
        