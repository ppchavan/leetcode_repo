# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Write your code here
        if head is None:
            return None
        
        # We need to keep track of all 3 nodes prev, curr and next for this. And keep updating all three nodes with each iteration.
        prev = None
        curr = head
        while curr:
            next_n = curr.next
            curr.next = prev
            prev = curr     
            curr = next_n
            
        return prev
        