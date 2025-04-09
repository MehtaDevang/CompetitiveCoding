"""
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:
    Input: head = [1,4,3,2,5,2], x = 3
    Output: [1,2,2,4,3,5]

Example 2:
    Input: head = [2,1], x = 2
    Output: [1,2]

Constraints:
    The number of nodes in the list is in the range [0, 200].
    -100 <= Node.val <= 100
    -200 <= x <= 200
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or head.next is None:
            return head

        current = head

        l1 = ListNode(0)
        l1_tail = l1

        l2 = ListNode(0)
        l2_tail = l2

        while current:
            if current.val < x:
                l1_tail.next = ListNode(current.val)
                l1_tail = l1_tail.next
            else:
                l2_tail.next = ListNode(current.val)
                l2_tail = l2_tail.next
            current = current.next
        
        l1_tail.next = l2.next

        return l1.next