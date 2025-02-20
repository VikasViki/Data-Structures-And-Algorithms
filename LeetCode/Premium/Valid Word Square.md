# Valid Word Square

## Description
Given a sequence of words, check whether it forms a valid word square. A sequence of words forms a valid word square if the k-th row and k-th column read the exact same string, where 0 ≤ k < max(numRows, numColumns).

## Example 1
```
Input:
[
  "abcd",
  "bnrt",
  "crmy",
  "dtye"
]

Output:
true

Explanation:
The first row and first column both read "abcd".
The second row and second column both read "bnrt".
The third row and third column both read "crmy".
The fourth row and fourth column both read "dtye".
Therefore, it is a valid word square.
```

## Example 2
```
Input:
[
  "abcd",
  "bnrt",
  "crm",
  "dt"
]

Output:
true

Explanation:
The first row and first column both read "abcd".
The second row and second column both read "bnrt".
The third row and third column both read "crm".
The fourth row and fourth column both read "dt".
Therefore, it is a valid word square.
```

## Example 3
```
Input:
[
  "ball",
  "area",
  "read",
  "lady"
]

Output:
false

Explanation:
The second row reads "area" while the second column reads "alrd".
Therefore, it is NOT a valid word square.
```

## Solution

```Python
from typing import (
    List,
)
from collections import defaultdict

class Solution:
    """
    @param words: a list of string
    @return: a boolean
    """
    def valid_word_square(self, words: List[str]) -> bool:
        row_word_len = defaultdict(int)
        col_word_len = defaultdict(int)
        total_rows = len(words)
        total_cols = len(words[0])

        for index, word in enumerate(words):
            word_len = len(word)
            row_word_len[index] = word_len
            for col in range(word_len):
                col_word_len[col] += 1
        
        k = max(total_rows, total_cols)
        for index in range(k):
            row_len = row_word_len[index]
            col_len = col_word_len[index]
            if row_len != col_len:
                return False
            
            row_word = ""
            for col in range(row_len):
                row_word += words[index][col]
            
            col_word = ""
            for row in range(col_len):
                col_word += words[row][index]        
            
            if row_word != col_word:
                return False
        
        return True
```

