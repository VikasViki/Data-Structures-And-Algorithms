# Question Link
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

# Approach

# Python Code

```Python
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0
        points.sort()
        prev_start, prev_end = points[0]
        arrows_count = 1
        for start, end in points[1:]:
            if start > prev_end:
                arrows_count += 1
                prev_start, prev_end = start, end
            else:
                prev_end = min(prev_end, end)
        return arrows_count
 ```

# Code Explanation
