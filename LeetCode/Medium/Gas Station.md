# Question Link
https://leetcode.com/problems/gas-station/

# Approach

# Python Code

```Python
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)-sum(cost) < 0:
            return -1
        
        total_stations = len(gas)
        
        first_station = 0
        current_gas = 0
        
        for index in range(total_stations):
            current_gas += gas[index]-cost[index]
            if current_gas < 0:
                first_station = index+1
                current_gas = 0
        
        return first_station
 ```

# Code Explanation
