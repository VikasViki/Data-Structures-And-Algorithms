# Question Link
https://leetcode.com/problems/first-missing-positive/

# Approach

# Python Code

```Python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_len = len(nums)
        
        for _ in range(4):
            
            for index in range(nums_len):
                curr_ele = nums[index]
                if index+1 != curr_ele and 0 < curr_ele < nums_len:
                    nums[index], nums[curr_ele-1] = nums[curr_ele-1], nums[index]


            for index in range(nums_len-1, -1, -1):
                curr_ele = nums[index]
                if index+1 != curr_ele and 0 < curr_ele < nums_len:
                    nums[index], nums[curr_ele-1] = nums[curr_ele-1], nums[index]
        
        print(nums)
        
        for index in range(nums_len):
            if index+1 != nums[index]:
                return index+1
        
        return nums_len+1
      
 ```

# Code Explanation
