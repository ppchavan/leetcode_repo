# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        # Breadth first search approach (BFS) explained in https://www.youtube.com/watch?v=6ZnyEApgFYg
        res = []        
        q = collections.deque()
        q.append(root)

        while q:
            q_len = len(q)
            level = []
            # Process through entire level
            for i in range(q_len):
                n = q.popleft()

                if n:
                    level.append(n.val)
                    q.append(n.left)
                    q.append(n.right)
            # After processing level, add it to result
            if level:
                res.append(level)
        return res

        
        