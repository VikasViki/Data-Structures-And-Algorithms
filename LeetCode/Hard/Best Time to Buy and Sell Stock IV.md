# Question Link
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

# Approach

# Python Code

```Python
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        prices_len = len(prices)
        if prices_len <= 1 or k == 0: return 0
        
        if k >= prices_len//2:
            profit = 0
            for index in range(1, prices_len):
                if prices[index] > prices[index-1]:
                    profit += prices[index]-prices[index-1]
            return profit
        
        MIN_VAL = -float('inf') 
        buy = [MIN_VAL] * k
        sell = [0] * k
        
        for price in prices:
            for day in range(k):
                buy[day] = max(buy[day], sell[day-1]-price if day != 0 else -price)
                sell[day] = max(sell[day], buy[day]+price)
        
        return sell[k-1]
        
```

# Code Explanation
