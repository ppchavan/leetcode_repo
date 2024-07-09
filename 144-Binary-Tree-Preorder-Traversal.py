# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        order = []
        def traverse(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            order.append(node.val)
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        return order
