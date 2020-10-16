# Question Link
https://leetcode.com/problems/rotate-array/

# Approach

# Python Code

```Python
class Solution:
    
    def reverse_list(self, arr, start, end):
        while start <= end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        k = k % nums_len
        
        self.reverse_list(nums, -k, -1)
        self.reverse_list(nums, -nums_len, -k-1)
        self.reverse_list(nums, 0, nums_len-1)
        
        
```

# Code Explanation
