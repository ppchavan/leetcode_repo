# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Post order traversal Left-Right-Root pattern
        order = []
        def traverse(node: Optional[TreeNode]) -> None:
            if node is None:
                return                
            traverse(node.left)            
            traverse(node.right)
            order.append(node.val)
        traverse(root)
        return order