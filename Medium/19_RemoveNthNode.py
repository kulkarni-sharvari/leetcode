# 19 - Remove Nth Node from end in a list - https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Example 2:
# Input: head = [1], n = 1
# Output: []

# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # calculate length of the list
        length = 0
        p1 = head
        while p1:
            length += 1
            p1 = p1.next


        if length == n:
            return head.next
        else:
            p1 = head
            for i in range(length - n - 1):
                p1 = p1.next
            p1.next = p1.next.next
            return head

# time complexity: Θ(n)
# space complexity: O(1)