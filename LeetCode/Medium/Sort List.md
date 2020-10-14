# Question Link
https://leetcode.com/problems/sort-list/

# Approach

# Python Code

```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    def find_mid(self, head):
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return mid
    
    def merge(self, left, right):
        if left.val <= right.val:
            top = left
            left = left.next
        else:
            top = right
            right = right.next
        
        curr = top
        
        while left and right:
            if left.val <= right.val:
                curr.next = left
                curr = left
                left = left.next
            else:
                curr.next = right
                curr = right
                right = right.next
        
        curr.next = left if left else right
        return top
    
    def merge_sort(self, head):
        if not head or not head.next: return head 
        
        mid = self.find_mid(head)
        left = self.merge_sort(head)
        right = self.merge_sort(mid)
        
        return self.merge(left, right)
        
    
    def sortList(self, head: ListNode) -> ListNode:
        return self.merge_sort(head)
        
```

# Code Explanation
