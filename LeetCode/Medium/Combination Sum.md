# Question Link
https://leetcode.com/problems/combination-sum/

# Approach

# Python Code

```Python
class Solution:
    def get_combinations(self, candidates, target, index, combination, curr_sum):
        if curr_sum > target or index == self.total_candidates:
            return
        
        if curr_sum == target:
            self.all_combinations.add(tuple(combination))
            return
        
        comb_copy = combination[:] 
        
        self.get_combinations(candidates, target, index, comb_copy+[candidates[index]],
                              curr_sum+candidates[index])
        
        self.get_combinations(candidates, target, index+1, comb_copy+[candidates[index]],
                              curr_sum+candidates[index])
        
        self.get_combinations(candidates, target, index+1, comb_copy, curr_sum)
        
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.total_candidates = len(candidates)
        self.all_combinations = set()
        self.get_combinations(candidates, target, 0, [], 0)
        
        return self.all_combinations
 ```

# Code Explanation
