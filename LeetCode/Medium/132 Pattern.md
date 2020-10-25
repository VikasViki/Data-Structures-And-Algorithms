# Question Link
https://leetcode.com/problems/132-pattern/

# Approach

# Python Code

## Time Complexity : O(N^3)

```Python
class Solution:
    def find_i(self, curr_index, curr_num):
        for index in range(curr_index):
            if self.nums[index] < curr_num:
                return index
    
    def find_j(self, start, end, curr_num):
        for index in range(start, end):
            if self.nums[index] > curr_num:
                return index
        
    def find132pattern(self, nums: List[int]) -> bool:
        self.nums = nums
        nums_len = len(self.nums)
        for index in range(2, nums_len):
            curr_num = nums[index]
            print(curr_num)
            i_index = self.find_i(index, curr_num)
            if i_index != None:
                if self.find_j(i_index, index, curr_num) != None:
                    return True
        
        return False          
 ```

## Code Explanation

## Time Complexity : 

```Python

            
 ```

## Code Explanation
