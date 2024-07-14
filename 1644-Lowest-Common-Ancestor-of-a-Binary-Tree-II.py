# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """ 
        These found flags are required since its not guaranteed if p and q are both present in given tree. 
        If either of them is not present in entire tree, we need to return None.
        """
        pfound = False
        qfound = False

        def dfs(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
            if not root:
                return None
            
            # Imp: to declare these flags as nonlocal. Otherwise the values are only modified "locally". But not passed outside of scope of recursive function.
            nonlocal pfound
            nonlocal qfound
            l = dfs(root.left, p, q)
            r = dfs(root.right, p, q)

            if root == p or root == q:
                if root == p:
                    pfound = True
                else:
                    qfound = True
                return root

            if l and r:
                return root
            else:
                return l or r

        ans = dfs(root, p, q)

        # Return ans only if both p and q were found, otherwise return None (since one of the p,q nodes was absent).
        return ans if pfound and qfound else None

# Time complexity is O(N) since we are doing a single traversal for entire tree