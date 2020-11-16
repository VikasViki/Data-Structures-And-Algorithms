# Question Link
https://leetcode.com/problems/flipping-an-image/

# Approach

# Python Code

```Python
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for index, row in enumerate(A):
            A[index] = [0 if pixel else 1 for pixel in row[::-1]]
        return A
            
 ```

# Code Explanation
