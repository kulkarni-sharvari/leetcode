# 23. Merge K Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/description/https://leetcode.com/problems/merge-k-sorted-lists/description/

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

# Example 1:
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted linked list:
# 1->1->2->3->4->4->5->6

# Example 2:
# Input: lists = []
# Output: []

# Example 3:
# Input: lists = [[]]
# Output: []
 

# Constraints:
# k == lists.length
# 0 <= k <= 104
# 0 <= lists[i].length <= 500
# -104 <= lists[i][j] <= 104
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 104.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        if not lists or k == 0:
            return None

        head1 = lists[0]
        
        for i in range(1, k):
            head = None
            head2 = lists[i]
            if not head1:
                head1 = head2
                continue

            if not head2:
                continue



            if head1.val<=head2.val:
                head = head1
                head1 = head1.next
            else:
                head = head2
                head2 = head2.next
            
            current = head

            while head1 and head2:
                if head1.val<=head2.val:
                    current.next = head1
                    head1 = head1.next
                else:
                    current.next = head2
                    head2 = head2.next
                current = current.next
            
            current.next = head1 or head2
            head1 = head

        return head1

# time complexity: Θ(kN) where k is length of lists and n is number of Nodes 
# space complexity: O(1)          


import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        dummy = ListNode(0)
        curr = dummy

        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
# time complexity: O(Nlgk) where k is length of lists and N is number of nodes.
# space complexity: O(N)