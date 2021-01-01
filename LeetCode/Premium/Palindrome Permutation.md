# Question Link
https://leetcode.com/problems/plus-one-linked-list/

# Approach

# Python Code

```Python
from collections import Counter
class Solution:
    """
    @param s: the given string
    @return: if a permutation of the string could form a palindrome
    """
    def canPermutePalindrome(self, s):
        # write your code here
        freq = Counter(s)
        odd_count = 0
        for count in freq.values():
            if count % 2:
                odd_count += 1
                if odd_count == 2:
                    return False
        return True
```

# Code Explanation
