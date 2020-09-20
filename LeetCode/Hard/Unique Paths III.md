# Question Link
https://leetcode.com/problems/unique-paths-iii/

# Approach

# Python Code

```Python
neighbours = [(0,-1), (0, 1), (-1,0), (1, 0)]

class Solution:
    
    def get_unique_paths_count(self, grid, row, col, zeros_count):
        if row < 0 or col < 0:
            return 
        
        if row >= self.total_rows or col >= self.total_cols:
            return
        
        if grid[row][col] == 2:
            if zeros_count == self.total_zeros:
                self.unique_paths_count += 1
            return
        
        elif grid[row][col] == 0:
            
            grid[row][col] = -1
            
            for x,y in neighbours:
                self.get_unique_paths_count(grid, row+x, col+y, zeros_count+1)
            
            grid[row][col] = 0
        
        return
    
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.unique_paths_count = 0
        
        self.total_rows = len(grid)
        self.total_cols = len(grid[0])
        
        start_row = start_col = 0
        self.total_zeros = 0
        
        for row in range(self.total_rows):
            for col in range(self.total_cols):
                if grid[row][col] == 0:
                    self.total_zeros += 1
                elif grid[row][col] == 1:
                    start_row = row
                    start_col = col
        
        grid[start_row][start_col] = -1
        for x, y in neighbours:
            self.get_unique_paths_count(grid, start_row+x, start_col+y, 0)
        
        return self.unique_paths_count
```

# Code Explanation
