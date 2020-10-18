# Question Link
https://leetcode.com/problems/search-a-2d-matrix/submissions/

# Approach

# Python Code

## Time Complexity : O(M*N)

```Python

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        total_rows = len(matrix)
        if not total_rows: return False
        
        total_cols = len(matrix[0])
        if not total_cols: return False
        
        for row in range(total_rows):
            for col in range(total_cols):
                if matrix[row][col] == target:
                    return True
        
        return False
 ```

## Code Explanation

## Time Complexity : O(M + N)

```Python
            
 ```

## Code Explanation

## Time Complexity : O(logM + logN)

```Python
            
 ```

## Code Explanation
