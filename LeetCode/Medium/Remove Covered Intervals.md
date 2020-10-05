# Question Link
https://leetcode.com/problems/remove-covered-intervals/

# Approach

# Python Code

```Python
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        new_intervals = [intervals[0]]
        
        for interval in intervals[1:]:
            prev_start, prev_end = new_intervals[-1]
            curr_start, curr_end = interval
            
            if prev_start <= curr_start and curr_end <= prev_end: continue
            if prev_start == curr_start and prev_end < curr_end: new_intervals.pop()
                
            new_intervals.append(interval)
        
        return len(new_intervals)
 ```

# Code Explanation
