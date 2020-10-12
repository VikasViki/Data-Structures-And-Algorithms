# Question Link
https://leetcode.com/problems/remove-duplicate-letters/

# Approach

# Python Code

```Python
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_index  = {}
        for index, char in enumerate(s):
            last_index[char] = index
        
        stack = []
        visited = set()
        s_len = len(s)
        
        for index in range(s_len):
            char = s[index]
            
            if char in visited : continue
            
            while stack and stack[-1] > char and last_index[stack[-1]] > index:
                visited.remove(stack[-1])
                stack.pop()
            
            stack.append(char)
            visited.add(char)
            
        return "".join(stack)
 ```

# Code Explanation
