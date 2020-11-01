# Question Link
https://leetcode.com/problems/maximize-distance-to-closest-person/

# Approach

# Python Code

## Time Complexity : 

```Python
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        total_seats = len(seats)
        seat_indices = []
        occupied_seats = 0
        for seat_index in range(total_seats):
            if seats[seat_index]:
                seat_indices += [seat_index]
                occupied_seats += 1
                
        max_distance = max(1,seat_indices[0])
        
        for index in range(occupied_seats-1):
            curr_distance = (seat_indices[index+1] - seat_indices[index])//2
            if curr_distance > max_distance:
                max_distance = curr_distance
        
        max_distance = max(max_distance, (total_seats-1)-seat_indices[-1] )
        
        return max_distance
 ```

## Code Explanation
