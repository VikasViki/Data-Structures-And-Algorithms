# Question Link
https://leetcode.com/problems/asteroid-collision/

# Approach

# Python Code

```Python
"""
class Solution:

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = [asteroids[0]]
        for asteroid in asteroids[1:]:
            if asteroid > 0:
                ans.append(asteroid)
            else:
                while ans and ans[-1] > 0:
                    if abs(ans[-1]) < abs(asteroid):
                        ans.pop()
                    else:
                        break
                if ans:
                    if ans[-1] < 0:
                        ans.append(asteroid)
                    else:
                        if abs(ans[-1]) == abs(asteroid):
                            ans.pop()
                else:
                    ans.append(asteroid)
        return ans
```

# Code Explanation
