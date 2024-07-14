# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Method 1
        This solution based on this video and does not make use of binary search property. Its solution for LC#236 Lowest common ancestor of a binary tree.
        https://www.youtube.com/watch?v=WO1tfq2sbsI&list=PLUPSMCjQ-7od5IVz8ug6D-apxFLkDTsoy&index=12
        if not root:
            return None
        
        if root == p or root == q:
            return root
        
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r:
            return root
        else:
            return l or r
        """
        """
        Method 2
        In case of binary search tree, we have a property that nodes from left subtree of current node have values less than the node. And nodes from right subtree have values greather than current node. So we make use of this property to traverse the tree. In this case, the time complexity is just height of subtree which is O(logN) so its faster than visiting each node in tree.
        * Explanation: https://www.youtube.com/watch?v=gs2LMfuOR9k
        """
        curr = root
        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr
