# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Recursive DFS approach. Swap values of left and right nodes and traverse it recursively (depth first).
        if root is None:
            return root
        
        def traverse(node: Optional[TreeNode])-> Optional[TreeNode]:
            if node is None:
                return node
            
            # swap the left and right values
            tmp = node.left
            node.left = node.right
            node.right = tmp
            traverse(node.left)
            traverse(node.right)
        
        traverse(root)
        return root

# Time and space complexity is linear O(N) where N is number of nodes in tree. 