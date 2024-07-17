from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:       
        adj_list = defaultdict(list)
        
        # Step 1. First create adj list for each node in graph
        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)
        
        # Step 2. Maintain a visited set to avoid inifinite loops
        visited = set()
        
        # Recursive DFS starting the source node. If we reach the destinate, we return True. If not, keep traversing using DFS method.
        def dfs(node):
            if node == destination:
                return True

            if node not in visited:                
                visited.add(node)

                for neighbour in adj_list[node]:                    
                    res = dfs(neighbour)                    
                    if res:
                        return True
            return False
        
        return dfs(source)

#Time complexity: O(V+E) where V is number of vertices and E is number of edges. So its linear.