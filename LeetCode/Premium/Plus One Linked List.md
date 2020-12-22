# Question Link
https://leetcode.com/problems/plus-one-linked-list/

# Approach

# Python Code

```Python
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the first Node
    @return: the answer after plus one
    """
    def plusOne(self, head):
        prev_node = None
        curr_node = head
        
        while curr_node:
            curr_node.prev = prev_node
            prev_node = curr_node
            curr_node = curr_node.next
            
        carry = 1
        curr_node = prev_node
        
        while curr_node:
            curr_val = curr_node.val + carry
            digit = curr_val % 10
            carry = 1 if curr_val > 9 else 0
            curr_node.val = digit
            curr_node = curr_node.prev
        
        if carry:
            return ListNode(1, head)
        
        return head
 ```

# Code Explanation
