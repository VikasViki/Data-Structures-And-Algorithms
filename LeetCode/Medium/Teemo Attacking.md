# Question Link
https://leetcode.com/problems/teemo-attacking/

# Approach

# Python Code

```Python
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if len(timeSeries) == 0:
            return 0
        
        total_duration = duration
        max_duration = timeSeries[0] + duration - 1
        
        for time in timeSeries[1:]:
            curr_duration = time + duration - 1
            
            if time <= max_duration:
                diff = curr_duration - max_duration
            else:
                diff = duration
                
            total_duration += diff
            max_duration = curr_duration
        
        return total_duration
 ```

# Code Explanation
