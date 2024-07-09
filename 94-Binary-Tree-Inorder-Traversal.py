# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # In order traversal Left-Root-Right pattern
        order = []
        def traverse(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            traverse(node.left)
            order.append(node.val)
            traverse(node.right)
        traverse(root)
        return order
        
        