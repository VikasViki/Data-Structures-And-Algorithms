# Question Link
https://leetcode.com/problems/add-two-numbers-ii/

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
    def get_values(self, node):
        stack = []
        if not node: return [0]
        while node:
            stack += [node.val]
            node = node.next
        return stack
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = self.get_values(l1)
        stack2 = self.get_values(l2)
        carry = 0
        prev_node = None
        
        while stack1 or stack2:
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0
            total_val = val1 + val2 + carry
            if total_val > 9:
                digit = total_val % 10
                carry = 1
            else:
                digit = total_val
                carry = 0
            
            curr_node = ListNode(digit)
            if prev_node:
                curr_node.next = prev_node
                
            prev_node = curr_node
        
        if carry:
            curr_node = ListNode(carry)
            curr_node.next = prev_node
        
        return curr_node
        
```

# Code Explanation
