# Question Link
https://leetcode.com/problems/word-break/

# Approach

# Python Code

```Python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dict_words = set(wordDict)
        
        s_len = len(s)
        is_word = [False] * (s_len+1)
        is_word[0] = True
        
        for start in range(s_len):
            if is_word[start]:
                for end in range(start+1, s_len+1):
                    if s[start:end] in dict_words:
                        is_word[end] = True
        
        return is_word[-1]
      
 ```

# Code Explanation
