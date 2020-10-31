# Question Link
https://leetcode.com/problems/summary-ranges/

# Approach

# Python Code

```Python
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        ranges = []
        nums_len = len(nums)
        start = nums[0]
        end = nums[0]
        for index in range(1,nums_len):
            if nums[index] == nums[index-1]+1:
                end = nums[index]
            else:
                if start < end:
                    ranges += [str(start)+'->'+str(end)]
                else:
                    ranges += [str(start)]
                start = nums[index]
        
        if start < end:
            ranges += [str(start)+'->'+str(end)]
        else:
            ranges += [str(start)]
            
        return ranges
 ```

# Code Explanation
