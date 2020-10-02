# Question Link
https://leetcode.com/problems/number-of-recent-calls/

# Approach

# Python Code

```Python
class RecentCounter:

    def __init__(self):
        self.ping_time = [] 
        

    def ping(self, t: int) -> int:
        self.ping_time.append(t)
        first_ping = t-3000
        count = 0
        for curr_ping in self.ping_time[::-1]:
            if curr_ping >= first_ping:
                count += 1
            else:
                break
        return count


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
      
 ```

# Code Explanation
