# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """ There are only three possible conditions for finding ancestor:
        1. We have a current node and the left and right nodes are p and q respectively. In this case, we return current node as ancestor.
        2. We have a hierarchy of nodes where p is current node and q is down the hierarchy (grandchild). In this case, common ancestor is p (since node is allowed to be a descendant of itself)
        3. We have a parent node as p and child node as q. Here parent node p is common ancestor.
        https://www.youtube.com/watch?v=WO1tfq2sbsI&list=PLUPSMCjQ-7od5IVz8ug6D-apxFLkDTsoy&index=12
        Based on this, we can come up with following solution using recursion.
        """
        if root is None:
            return None
        
        if root == p or root == q:
            return root
        
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        
        # If both nodes are non null, then it means p is located in left subtree and q is found in right subtree. So our ancestor is root itself.
        if l and r:
            return root
        
        # If previous conditions were not satisfied and then check if l or r are valid nodes. Whichever is non null is the ancestor. If both are null, then there is no ancestor.
        return l or r

# Time complexity is O(N) since in worst case scenario, we traverse the whole tree once.