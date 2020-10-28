# Question Link
https://leetcode.com/problems/champagne-tower/

# Approach

# Python Code

```Python
"""
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        glass = [poured]
        
        for row in range(query_row):
            temp_glass = [0] * (len(glass)+1)
            for index in range(len(glass)):
                pour = (glass[index]-1)/2
                if pour > 0:
                    temp_glass[index] += pour
                    temp_glass[index+1] += pour
            glass = temp_glass
        
        return min(1, glass[query_glass])
                    
```

# Code Explanation
