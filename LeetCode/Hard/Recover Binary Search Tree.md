# Question Link
https://leetcode.com/problems/recover-binary-search-tree/

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
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        tree = []
        
        def inorder(root, tree):
            if not root: return []
            inorder(root.left, tree)
            tree += [root]
            inorder(root.right, tree)
        
        inorder(root, tree)
        
        bst = sorted(tree, key = lambda x:x.val)
        
        node1 = node2 = None
        
        for index in range(len(tree)):
            if tree[index].val != bst[index].val:
                tree[index].val, bst[index].val = bst[index].val, tree[index].val
                break
```

# Code Explanation
