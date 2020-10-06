# Question Link
https://leetcode.com/problems/complement-of-base-10-integer/

# Approach

# Python Code

```Python
class Solution:
    def bitwiseComplement(self, N):
        
        if N == 0:
            return 1
        
        # Getting binary complement of N
        
        comp_num = 0
        power_val = 0
        
        while N > 0:
            rem = N%2
            if rem == 0:
                comp_num += 2**(power_val)
                
            power_val += 1
            N = N//2
        
        return comp_num
 ```

# Code Explanation
