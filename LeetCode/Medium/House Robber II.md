# Question Link
https://leetcode.com/problems/house-robber-ii/

# Approach

# Python Code

```Python
class Solution:
    def rob(self, nums: List[int]) -> int:
        nums_len = len(nums)
        
        if nums_len < 2: return max(nums)
        
        money = [0] * nums_len
        money[0] = nums[0]
        money[1] = max(nums[0], nums[1])
        
        for index in range(2, nums_len-1):
            money[index] = max(nums[index]+money[index-2], money[index-1])
        
        ans1 = money[-2]
        
        money = [0] * nums_len
        money[1] = nums[1]
        for index in range(2, nums_len):
            money[index] = max(nums[index]+money[index-2], money[index-1])
        
        ans2 = money[-1]
        
        return max(ans1, ans2)
```

# Code Explanation
