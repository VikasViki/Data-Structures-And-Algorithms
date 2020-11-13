# Question Link
https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

# Approach

# Python Code

```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        max_diff = float('-inf')
        visited = set()
        stack = [root]
        
        while stack:
            node = stack[-1]
            left_node = node.left
            right_node = node.right
            
            if left_node and left_node not in visited:
                stack.append(left_node)
            
            elif right_node and right_node not in visited:
                stack.append(right_node)
                    
            else:
                if not left_node and not right_node:
                    min_node = min(stack, key = lambda x:x.val)
                    max_node = max(stack, key = lambda x:x.val)
                    max_diff = max(max_diff, abs(max_node.val-min_node.val))
                
                top = stack.pop()
                visited.add(top)
        
        return max_diff
         
 ```

# Code Explanation
