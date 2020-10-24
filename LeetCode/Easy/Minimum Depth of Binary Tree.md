# Question Link
https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Approach

# Python Code

```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    
    def is_leaf(self, node):
        return not node.left and not node.right
    
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        
        if self.is_leaf(root): return 1
        
        queue = deque([(root,1)])
        while queue:
            curr, count = queue.popleft()
            if self.is_leaf(curr):
                    return count
            
            if curr.left:
                queue.append((curr.left, count+1))
            
            if curr.right:
                queue.append((curr.right, count+1))
        
        #return min_depth
                
        
        
 ```

# Code Explanation
