# 143. Reorder List - https://leetcode.com/problems/reorder-list/description/

# ################################# DESCRIPTION ################################

# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

# ################################## EXAMPLE ###################################
# Example 1
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]

# Example 2:
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        array_nodes = list()
        p1 = head
        while p1:
            array_nodes.append(p1)
            p1 = p1.next

        n = len(array_nodes)
        left = 1
        right = n - 1
        p1 = head
        while left < right:
            left_node = array_nodes[left]
            right_node = array_nodes[right]
            p1.next = right_node
            p1 = p1.next
            p1.next = left_node
            p1 = p1.next
            left += 1
            right -= 1
        p1.next = array_nodes[right]
        p1.next.next = None


# Time complexity: Θ(n)
# Space complexity: Θ(n)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        size = 0

        # find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next=prev
            prev=second
            second = temp
        
        #Merge

        # head has 1st half of the list
        # prev has 2nd half of list but in reverse order.
        first = head
        while prev:
            temp1, temp2 = first.next, prev.next
            first.next=prev
            prev.next=temp1
            first = temp1
            prev=temp2

# Time complexity: Θ(n)
# Space complexity: O(1)
            