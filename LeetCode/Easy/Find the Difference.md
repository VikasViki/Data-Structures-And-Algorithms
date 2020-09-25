# Question Link
https://leetcode.com/problems/find-the-difference/

# Approach

# Python Code

```Python
from collections import Counter
from string import ascii_lowercase

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_freq = Counter(s)
        t_freq = Counter(t)
        for char in ascii_lowercase:
            if s_freq[char] != t_freq[char]:
                return char
 ```

# Code Explanation

