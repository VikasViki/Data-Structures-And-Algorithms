# Question Link
https://leetcode.com/problems/number-of-longest-increasing-subsequence/

# Approach

# Python Code

```Python
"""
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        
        nums_len = len(nums)
        length = [1] * nums_len
        count = [1] * nums_len
        
        lis = 1
        
        for i in range(1, nums_len):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    if length[j]+1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = count[j]
                    elif length[j]+1 == length[i]:
                        count[i] += count[j]
            lis = max(lis, length[i])
        
        ans = 0
        for index in range(nums_len):
            if length[index] == lis:
                ans += count[index]
        
        return ans
```

# Code Explanation
