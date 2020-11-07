# Question Link
https://leetcode.com/problems/consecutive-characters/

# Approach

# Python Code

```Python
class Solution:
    def maxPower(self, s: str) -> int:
        max_power = power = 1
        s_len = len(s)
        
        for index in range(1, s_len):
            if s[index] == s[index-1]:
                power += 1
            else:
                max_power = max(max_power, power)
                power = 1
        
        return max(max_power, power)
 ```

# Code Explanation
