# Question Link
https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/

# Approach

# Python Code

```Python
from collections import defaultdict

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        chips_at_position = defaultdict(int)
        for chip_position in position:
            chips_at_position[chip_position] += 1
        
        chips_at_odd = chips_at_even = 0
        for chip_position, chip_count in chips_at_position.items():
            if chip_position % 2:
                chips_at_odd += chip_count
            else:
                chips_at_even += chip_count
        
        return min(chips_at_odd, chips_at_even)
 ```

# Code Explanation
