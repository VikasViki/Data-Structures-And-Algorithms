# Question Link
https://leetcode.com/problems/buddy-strings/

# Approach

# Python Code

```Python
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        mismatch = 0
        A_len = len(A)
        B_len = len(B)
        
        if A_len != B_len:
            return False
        
        diff = []
        for index in range(A_len):
            if A[index] != B[index]:
                mismatch += 1
                diff.append((A[index],B[index]))
                if mismatch == 3:
                    return False
        
        if mismatch == 2:
            a1, b1 = diff[0]
            a2, b2 = diff[1]
            if a1 == b2 and a2 == b1:
                return True
            else:
                return False
        
        if mismatch == 0:
            freq = {}
            for char in A:
                freq[char] = freq.get(char, 0) + 1
                if freq[char] == 2:
                    return True
            return False
            
        return False
 ```

# Code Explanation
