"""
Given the head of a linked list, rotate the list to the right by k places.

Example 1:
    Input: head = [1,2,3,4,5], k = 2
    Output: [4,5,1,2,3]

Example 2:
    Input: head = [0,1,2], k = 4
    Output: [2,0,1]

Constraints:
    The number of nodes in the list is in the range [0, 500].
    -100 <= Node.val <= 100
    0 <= k <= 2 * 109
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0

        if k == 0 or not head:
            return head

        temp = head
        while temp:
            n += 1
            temp = temp.next

        
        k = k % n

        if n == 1 or k == 0:
            return head

        n_l1 = n - k
        n_l2 = k

        temp = head
        x = 1

        while x < n_l1:
            temp = temp.next
            x += 1

        l2_head = temp.next
        temp.next = None

        temp = l2_head
        while temp.next is not None:
            temp = temp.next
        temp.next  = head

        head = l2_head

        return head
        