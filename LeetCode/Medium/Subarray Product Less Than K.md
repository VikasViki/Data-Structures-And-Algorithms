# Question Link
https://leetcode.com/problems/subarray-product-less-than-k/

# Approach

# Python Code

```Python
class Solution:
    
    def get_subarr_count(self, start, end):
        ele_count = end-start
        return (ele_count * (ele_count+1)) // 2
    
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        total_subarr = 0
        
        if k == 0:
            return total_subarr
        
        nums_len = len(nums)
        
        start = 0
        end = 0
        prev_end = 0
        
        curr_prod = 1
        
        while end < nums_len:
            curr_prod *= nums[end]
            
            while start < nums_len and curr_prod >= k:
                total_subarr += self.get_subarr_count(start, end)
                total_subarr -= self.get_subarr_count(start, prev_end)
                
                curr_prod /= nums[start]
                start += 1
                prev_end = end
            
            end += 1
        
        if curr_prod < k:
            total_subarr += self.get_subarr_count(start, end)
            total_subarr -= self.get_subarr_count(start, prev_end)
        
        
        return total_subarr
 ```

# Code Explanation
