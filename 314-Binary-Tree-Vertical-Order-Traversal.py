# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Explanation of solution: https://www.youtube.com/watch?v=xpXoHCFYC5c
        if root is None:
            return []
        
        # Answer: https://www.youtube.com/watch?v=xpXoHCFYC5c
        # This approach is combination of BFS and using a map to maintain x coordinate of a node.
        # We traverse the tree using BFS approach and maintain a map of x coordinate of a node. Root node is assigned (0,0) coordinates.
        # So nodes to left of root will have negative and right of root will have positive coordinates.
        # We then maintain a map of x coordinate as key and node values in a list (there could be multiples nodes belonging to a single x coodinate).
        # Later, we have to traverse the map from min to max x and add a list corresponding to each x-cordinates to results list.
        q = collections.deque()
        m = collections.defaultdict(list)
        xset = set()
        res = []
        # Use a queue of tuples, first element represents x coordinate and second element is node value
        q.append((0, root))

        # Start BFS traversal
        while q:
            x, node = q.popleft()

            m[x].append(node.val)
            xset.add(int(x))

            if node.left:
                q.append((x-1, node.left))
            if node.right:
                q.append((x+1, node.right))
        
        # Get sorted list from set of x co-ordinates
        xlist = sorted(xset)
        for level in xlist:
            print(level)
            res.append(m[level])
        
        return res        
        