# Question Link
https://leetcode.com/problems/repeated-dna-sequences/

# Approach

# Python Code

```Python
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if not s: return []
        s_len = len(s)
        
        start, end = 0, 10
        dna_freq = {}
        
        while end <= s_len:
            dna_seq = s[start:end]
            dna_freq[dna_seq] = dna_freq.get(dna_seq, 0) + 1
            start += 1
            end += 1
            
        ans = []
        
        for seq, count in dna_freq.items():
            if count > 1:
                ans += [seq]
        
        return ans  
```

# Code Explanation
