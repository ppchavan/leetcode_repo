class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # Start point should be at (0, 0) location
        # End point is at (n-1, n-1) location and both start and end points must be 0. 
        # Otherwise there is no path.        
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        
        # Since its a binary square grid, we only need to keep track of side of square (n)
        n = len(grid) 
        # Initialize path_length to 1 since we always start from 0 and it should be counted
        path_len = 1
        
        # Start at (0, 0) position and add it to queue
        q = collections.deque([(0, 0, path_len)])
        
        # Important: Mark the point at (0, 0) coordinate to be 1
        grid[0][0] = 1

        # These are 8 possible directions for movement on the grid
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        while q:
            x, y, path_len = q.popleft()

            if (x, y) == (n-1, n-1):
                return path_len
            
            # Iterate over directions
            for dx, dy in dirs:
                newx, newy = x+dx, y+dy
         
                if (0 <= newx < n) and (0 <= newy < n) and grid[newx][newy] == 0:
                    grid[newx][newy] = 1
                    q.append((newx, newy, path_len+1))
        
        return -1

# Time complexity is linear O(N) since we visit all nodes in worst case.

