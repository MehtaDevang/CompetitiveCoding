"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.


Example 1:
    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]

Example 2:
    Input: list1 = [], list2 = []
    Output: []

Example 3:
    Input: list1 = [], list2 = [0]
    Output: [0]

Constraints:
    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = list1
        temp2 = list2

        new_head = None
        temp = None
        while temp1 and temp2:
            v1 = temp1.val
            v2 = temp2.val

            if v1 <= v2:
                node = temp1
                temp1 = temp1.next
            else:
                node = temp2
                temp2 = temp2.next
            

            if not new_head:
                new_head = node
                temp = new_head
            else:
                temp.next = node
                temp = temp.next
        
        while temp1 is not None:
            if not new_head:
                new_head = temp1
                temp1 = temp1.next
                temp = new_head
            else:
                temp.next = temp1
                temp1 = temp1.next
                temp = temp.next
        
        while temp2 is not None:
            if not new_head:
                new_head = temp2
                temp2 = temp2.next
                temp = new_head
            else:
                temp.next = temp2
                temp2 = temp2.next
                temp = temp.next
        
        return new_head
            