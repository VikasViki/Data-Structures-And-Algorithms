# Question Link
https://leetcode.com/problems/binary-search/

# Approach

# Python Code

```Python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums_len = len(nums)
        start = 0 
        end = nums_len -1
        
        while start <= end:
            mid = (start+end)//2
            if  nums[mid] < target:
                start = mid + 1
                
            elif nums[mid] > target:
                end = end - 1
            else:
                return mid
        
        return -1
 ```

# Code Explanation
