# Question Link
https://leetcode.com/problems/missing-ranges/

# Approach

# Python Code

```Python
class Solution:
    """
    @param: nums: a sorted integer array
    @param: lower: An integer
    @param: upper: An integer
    @return: a list of its missing ranges
    """
    
    def append_range(self, diff, lower , upper=None):
        if diff == 2:
            self.missing_ranges += [str(lower)]
        elif diff > 2:
            self.missing_ranges += ["{0}->{1}".format(lower, upper)]
    
    
    def findMissingRanges(self, nums, lower, upper):
        # write your code here
        self.missing_ranges = []
        
        if not nums: 
            if lower == upper:
                return [str(lower)]
            return ["{0}->{1}".format(lower, upper)]
            
        nums_len = len(nums)
        
        diff = nums[0]-lower + 1
        self.append_range(diff, lower, nums[0]-1)
        
        for index in range(nums_len-1):
            diff = nums[index+1] - nums[index]
            self.append_range(diff, nums[index]+1, nums[index+1]-1)
        
        diff = upper - nums[-1] + 1
        self.append_range(diff, nums[-1]+1, upper)
        
        return self.missing_ranges
 ```

# Code Explanation
