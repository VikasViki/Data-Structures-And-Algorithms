# Question Link
https://leetcode.com/problems/insertion-sort-list/

# Approach

# Python Code

```Python
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        
        i_ptr = head
        while i_ptr:
            j_ptr = i_ptr.next
            temp = i_ptr
            while j_ptr:
                if j_ptr.val < temp.val:
                    temp = j_ptr
                j_ptr = j_ptr.next
            i_ptr.val, temp.val = temp.val, i_ptr.val
            i_ptr = i_ptr.next
        
        return head
```

# Code Explanation
