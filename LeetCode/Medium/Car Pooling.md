# Question Link
https://leetcode.com/problems/car-pooling/

# Approach

# Python Code

```Python

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips_length = len(trips)
        
        if trips_length == 0:
            return True
        
        location = [0] * 1001
        
        for passengers, start, end in trips:
            
            for index in range(start, end):
                location[index] += passengers
                if location[index] > capacity:
                    return False
        
        return True
 ```

# Code Explanation
