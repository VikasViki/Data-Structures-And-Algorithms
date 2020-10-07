# Question Link
https://leetcode.com/problems/insert-into-a-binary-search-tree/

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
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        curr = root
        
        while curr:
            if val > curr.val:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = TreeNode(val)
                    break
            else:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = TreeNode(val)
                    break
        
        return root if root else TreeNode(val)
         
 ```

# Code Explanation
