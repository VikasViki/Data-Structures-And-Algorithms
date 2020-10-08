# Question Link
https://leetcode.com/problems/rotate-list/

# Approach

# Python Code

```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        total_nodes = 0
        curr = head
        while curr:
            curr = curr.next
            total_nodes += 1
        
        if total_nodes == 0:
            return None
        
        k = k % total_nodes
        
        start = head
        end = head
        while k:
            end = end.next
            k -= 1
        
        while end.next:
            start = start.next
            end = end.next
        
        end.next = head
        new_head = start.next
        start.next = None
        
        return new_head
 ```

# Code Explanation
