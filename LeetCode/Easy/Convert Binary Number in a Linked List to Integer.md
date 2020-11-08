# Question Link
https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

# Approach

- Traverse the link list from left to right
- While traversing store values of node into a concatenated string
- Multiply the string value with 2<sup>index</sup> 
- Store the accumalted sum in a decimal variable

# Python Code

```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binary_str = ""
        binary_len = 0
        curr = head
        
        while curr:
            binary_str = str(curr.val) + binary_str
            binary_len += 1
            curr = curr.next
        
        decimal_val = 0
        for index in range(binary_len):
            if binary_str[index] == '1':
                decimal_val += 2**(index)
        
        return decimal_val
 ```

# Code Explanation
