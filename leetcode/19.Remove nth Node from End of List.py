"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
Example 1
    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]

Example 2:
    Input: head = [1], n = 1
    Output: []

Example 3:
    Input: head = [1,2], n = 1
    Output: [1]
 

Constraints:
    The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # count the length of the list
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        
        # get the nth node
        nth_node_from_last = length - n + 1

        if nth_node_from_last == 1:
            head = head.next
            return head
        
        current_index = 2
        temp = head

        # get to n - 1 th node and make its next to the next if nth node 
        while current_index < nth_node_from_last:
            temp = temp.next
            current_index += 1
        temp.next = temp.next.next
        
        return head
        