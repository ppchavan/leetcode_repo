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
        q = collections.deque([root])
        res = []

        while q:
            level = []
            # This variable is necessary to record the length of queue before we start for loop, since we will append nodes. So length may change later.         
            qlen = len(q)
            # This for loop is necessary to go over all nodes in a particular level
            for i in range(qlen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            # After for loop ends, processing for a single level is finished so add to result   
            res.append(level)

        return res        

# Time complexity is O(N) since we visit each node in tree only once.