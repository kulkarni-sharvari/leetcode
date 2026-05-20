# 21. Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/description/

# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: list1 = [], list2 = []
# Output: []

# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        curr = None
        resultantHead = None
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            curr = list1
            resultantHead = list1
            p1 = list1.next
            p2 = list2
        else:
            curr = list2
            resultantHead = list2
            p1 = list2.next
            p2 = list1

        while p1 and p2:
            if p1.val <= p2.val:
                curr.next = p1
                p1 = p1.next
            else:
                curr.next = p2
                p2 = p2.next
            curr = curr.next
        if p1 != None:
            curr.next = p1
        if p2 != None:
            curr.next = p2
        return resultantHead