# Question Link
https://leetcode.com/problems/evaluate-division/

# Approach

# Python Code

```Python
from collections import deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        
        equations_len = len(equations)
        
        for index in range(equations_len):
            source, dest = equations[index]
            weight = values[index]
            
            graph[source][dest] = weight
            graph[dest][source] = 1/weight
        
        
        ans = []
        
        for src, dest in queries:
            
            if src not in graph or dest not in graph:
                ans.append(-1)
            
            elif src == dest :
                ans.append(1)
            
            else:
                queue = deque([(src,1.0)])
                visited = set([src])
                dest_found = False
                while queue:
                    node, weight = queue.popleft()
                    for child in graph[node]:
                        new_weight = weight * graph[node][child] 
                        if child == dest:
                            ans.append(new_weight)
                            dest_found = True
                            break

                        if child not in visited:
                            visited.add(child)
                            queue.append((child, new_weight))
                    
                    if dest_found:
                        break
                        
                if not dest_found:
                    ans.append(-1)
        
        return ans
 ```

# Code Explanation
