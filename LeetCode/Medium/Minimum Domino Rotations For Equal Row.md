# Question Link
https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

# Approach

# Python Code

```Python
class Solution:
    
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        total_dominos = len(A)
        
        A_freq = {}
        B_freq = {}
        AB_freq = {}
        for index in range(total_dominos):
            A_freq[A[index]] = A_freq.get(A[index], 0) + 1
            B_freq[B[index]] = B_freq.get(B[index], 0) + 1
            if A[index] != B[index]:
                AB_freq[A[index]] = AB_freq.get(A[index], 0) + 1
                AB_freq[B[index]] = AB_freq.get(B[index], 0) + 1
            else:
                AB_freq[A[index]] = AB_freq.get(A[index], 0) + 1
        
        swap_possible = False
        for val, freq in AB_freq.items():
            if freq >= total_dominos:
                swap_possible = True
                break
        
        if not swap_possible: return -1
        
        A_min_swap = float('inf')
        B_min_swap = float('inf')
        for val, freq in AB_freq.items():
            if AB_freq[val] == total_dominos:
                A_min_swap = min(A_freq[val], total_dominos-A_freq[val])
                B_min_swap = min(B_freq[val], total_dominos-B_freq[val])
        
        return min(A_min_swap, B_min_swap)
```

# Code Explanation
