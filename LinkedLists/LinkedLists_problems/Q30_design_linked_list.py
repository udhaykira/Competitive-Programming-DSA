"""
LeetCode : 707
Design Linked List

Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.

Example 1:

Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3

"""
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index):
        curr = self.head

        for _ in range(index):
            if not curr:
                return -1
            curr = curr.next

        return curr.val if curr else -1

    def addAtHead(self, val):
        node = ListNode(val)
        node.next = self.head
        self.head = node

    def addAtTail(self, val):
        node = ListNode(val)

        if not self.head:
            self.head = node
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = node

    def addAtIndex(self, index, val):
        if index == 0:
            self.addAtHead(val)
            return

        curr = self.head

        for _ in range(index - 1):
            if not curr:
                return
            curr = curr.next

        if not curr:
            return

        node = ListNode(val)
        node.next = curr.next
        curr.next = node

    def deleteAtIndex(self, index):
        if not self.head:
            return

        if index == 0:
            self.head = self.head.next
            return

        curr = self.head

        for _ in range(index - 1):
            if not curr:
                return
            curr = curr.next

        if curr and curr.next:
            curr.next = curr.next.next