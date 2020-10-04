# Question Link
https://leetcode.com/problems/k-diff-pairs-in-an-array/

# Approach

# Python Code

```Python
class Solution:
    def pair_exist(self, nums: List[int], start: int, end: int, target: int) -> bool:
        while start <= end:
            mid = (start+end)//2
            if nums[mid] > target:
                end = mid-1
            elif nums[mid] < target:
                start = mid + 1
            else:
                return True
        return False
    
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        nums_len = len(nums)
        
        pairs_count = int(self.pair_exist(nums, 1, nums_len-1, nums[0]+k))
        
        for index in range(1,nums_len):
            if nums[index] != nums[index-1]:
                target = nums[index]+k
                if self.pair_exist(nums, index+1, nums_len-1, target):
                    pairs_count += 1
        
        return pairs_count
 ```

# Code Explanation
