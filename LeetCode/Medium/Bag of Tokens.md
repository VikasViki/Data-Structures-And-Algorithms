# Question Link
https://leetcode.com/problems/bag-of-tokens/submissions/

# Approach

# Python Code

```Python
"""
class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        if not tokens or not P: return 0
        tokens.sort()
        score = 0
        power = P
        start = 0
        end = len(tokens)-1
        
        while start < end:
            if tokens[start] <= power:
                power -= tokens[start]
                score += 1
                start += 1
            else:
                if not score: return 0
                score -= 1
                power += tokens[end]
                end -= 1
        
        if power >= tokens[start]:
            score += 1
            power -= tokens[start]
                
        return score
        
```

# Code Explanation
