# Question Link
https://leetcode.com/problems/stone-game-iv/

# Approach

# Python Code

```Python
"""
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        win = [False] * (n+1)
        
        for index in range(1, n+1):
            for square in range(1, int(index**0.5)+1):
                if win[index-square**2] == False:
                    win[index] = True
        
        return win[n]
        
```

# Code Explanation
