# Question Link
https://leetcode.com/problems/clone-graph/

# Approach

# Python Code

```Python
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        
        hash_map = {node:Node(node.val)}
        
        queue = deque([node])
        traversed = set([node])
        
        while queue:
            curr = queue.popleft()
            parent = hash_map.get(curr)
            for neighbor in curr.neighbors:
                hash_map[neighbor] = hash_map.get(neighbor, Node(neighbor.val))
                child = hash_map[neighbor]
                parent.neighbors.append(child)
                if neighbor not in traversed:
                    queue.append(neighbor)
                    traversed.add(neighbor)
        
        return hash_map[node]
```

# Code Explanation
