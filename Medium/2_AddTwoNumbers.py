# 2. Add two numbers - https://leetcode.com/problems/add-two-numbers/description/

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        
        curr = ans = ListNode(0, None)
        carry = 0
        while l1 or l2 or carry:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            add = num1+num2+carry
            digit = add%10
            carry = add//10
            curr.next = ListNode(digit, None)
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return ans.next


# time complexity: Θ(max(n,m)) where m is length of l1 and n is length of l2.
# space complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        stack1 = ""
        stack2 = ""
        answer = ""

        p1 = l1
        while p1:
            stack1 += str(p1.val)
            p1 = p1.next
        num1 = int("".join(reversed(stack1)))

        p1 = l2
        while p1:
            stack2 += str(p1.val)
            p1 = p1.next
        num2 = int("".join(reversed(stack2)))
        num3 = num1 + num2
        newHead = prev = None

        if num3 == 0:
            return ListNode(0, None)

        while num3 != 0:
            node = ListNode(num3 % 10, None)
            if not newHead:
                newHead = node
            if prev:
                prev.next = node
            prev = node
            num3 = num3 // 10
        return newHead

# time complexity: Θ(m+n+ans) where m is length of l1, n is length of l2 and ans is length of answer
# space complexity: O(m+n+ans)
