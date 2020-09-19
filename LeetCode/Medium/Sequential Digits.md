Question Link : https://leetcode.com/problems/sequential-digits/

Approach :

Solution:

```Python
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        
        digits = "123456789"
        
        str_low = str(low)
        str_high = str(high)
        
        low_digits_count = len(str_low)
        high_digits_count = len(str_high)
        
        for size in range(low_digits_count, high_digits_count+1):
            for index in range(10-size):
                num = digits[index:index+size]
                if low <= int(num) <= high:
                    ans.append(num)
        
        return ans
```
