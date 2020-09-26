# Question Link
https://leetcode.com/problems/largest-number/

# Approach

# Python Code

## Time Complexity : O(N^2)

```Python

class Solution:
    def check_swap(self, str_nums, i, j):
        without_swap = str_nums[i] + str_nums[j]
        with_swap = str_nums[j] + str_nums[i]
        if with_swap > without_swap:
            return True
        return False
        
    def largestNumber(self, nums: List[int]) -> str:
        total_nums = len(nums)
        str_nums = list(map(str, nums))
        
        for i in range(total_nums):
            for j in range(i+1, total_nums):
                if self.check_swap(str_nums, i, j):
                    str_nums[i], str_nums[j] = str_nums[j], str_nums[i]
                    
        new_str = "".join(str_nums)
        if set(new_str) == {'0'}:
            return '0'
        
        return new_str
            
 ```

## Code Explanation

## Time Complexity : O(NlogN)

```Python

from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = list(map(str, nums))
        
        def compare(str1, str2):
            if str1+str2 < str2+str1:
                return 1
            return -1
        
        sorted_str = sorted(str_nums, key=cmp_to_key(compare))
        
        if sorted_str[0] == '0':
            return '0'
        
        return "".join(sorted_str)
            
 ```

## Code Explanation
