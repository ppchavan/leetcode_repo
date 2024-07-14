# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def checkBST(node: TreeNode, minv, maxv) -> bool:
            if not node:
                return True
            if not (minv < node.val and node.val < maxv):
                return False

            l = checkBST(node.left, minv, node.val)
            r = checkBST(node.right, node.val, maxv)
            return l and r
        
        return checkBST(root, float("-inf"), float("inf"))

# Time complexity is linear O(N) since in worst case, we go through every node in the tree.