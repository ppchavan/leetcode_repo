# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        mid = head
        cnt = 0

        while head is not None:
            # Increment mid only if count is odd
            if cnt % 2 != 0:
                mid = mid.next
            cnt += 1
            head = head.next
        
        return mid

# Time complexity: O(N)
