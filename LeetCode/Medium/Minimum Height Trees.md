# Question Link
https://leetcode.com/problems/minimum-height-trees/

# Approach

# Python Code

```Python
from collections import defaultdict, deque

class Graph:
    def __init__(self, total_vertices, edges):
        self.total_vertices = total_vertices
        self.edges = edges
        self.create_graph()
    
    def create_graph(self):
        self.degree = defaultdict(int)
        self.graph = defaultdict(list)
        
        for parent, child in self.edges:
            self.graph[parent].append(child)
            self.graph[child].append(parent)
            
            self.degree[parent] += 1
            self.degree[child] += 1
    
    def get_min_height_nodes(self):
        queue = deque()
        for node in range(self.total_vertices):
            if self.degree[node] == 1:
                queue.append(node)
        
        total_nodes = self.total_vertices
        
        while total_nodes > 2:
            queue_len = len(queue)
            total_nodes -= queue_len
            
            while queue_len:
                node = queue.popleft()
                for child in self.graph[node]:
                    self.degree[child] -= 1
                    if self.degree[child] == 1:
                        queue.append(child)
                queue_len -= 1
                
        return queue
        

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]
        graph = Graph(n, edges)
        return graph.get_min_height_nodes()
        
```

# Code Explanation
