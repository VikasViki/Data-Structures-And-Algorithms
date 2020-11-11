# Question Link
https://leetcode.com/problems/binary-tree-tilt/

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
    
    def post_order(self, node: TreeNode) -> None:
        if not node: return None
        
        self.post_order(node.left)
        self.post_order(node.right)
        
        left_tree_sum = node.left.sum if node.left else 0
        right_tree_sum = node.right.sum if node.right else 0
        
        node.sum = left_tree_sum + right_tree_sum + node.val
        self.tilt_val += abs(left_tree_sum - right_tree_sum)
        
    
    def findTilt(self, root: TreeNode) -> int:
        self.tilt_val = 0
        self.post_order(root)
        
        return self.tilt_val
        
 ```

# Code Explanation
