# Question Link
https://leetcode.com/problems/linked-list-cycle-ii/

# Approach

# Python Code

```Python
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        curr = head
        while curr and curr.val != '*':
            curr.val = '*'
            curr = curr.next
        
        if not curr or curr.val != '*': return None
        
        return curr
            
        
```

# Code Explanation
