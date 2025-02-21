# Word Squares

## Problem Statement
A **word square** is an arrangement of words in a square grid such that the \( k \)-th row and \( k \)-th column contain the same string, for all valid \( k \).

Given a list of unique words, return all possible word squares.

## Example

### Input:
```plaintext
words = ["area", "lead", "wall", "lady", "ball"]
```

### Output:
```plaintext
[
  ["wall",
   "area",
   "lead",
   "lady"],

  ["ball",
   "area",
   "lead",
   "lady"]
]
```

## Constraints
- The number of words is at least **1** and at most **1000**.
- All words have the **exact same length**.
- The length of each word is at least **1** and at most **5**.
- Each word consists of **only lowercase English letters** (a-z).

## Approach
To efficiently generate word squares, consider using a **Trie (prefix tree)** for quick prefix lookups. This helps in pruning invalid paths early.

### Steps:
1. **Build a Trie** from the given words.
2. **Use Depth-First Search (DFS)** to construct word squares.
3. **Backtracking** ensures only valid word sequences are explored.

## Python Solution
```python
from collections import deque

class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.prefix_words_list = []
    
    def __repr__(self):
        return f"{self.char} -> {self.prefix_words_list}"

class Trie:
    def __init__(self):
        self.root = TrieNode('*')
    
    def add_word_to_trie(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children.get(char)
            else:
                child_node = TrieNode(char)
                node.children[char] = child_node
                node = child_node
            node.prefix_words_list.append(word)
    
    def find_word_with_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return [] # prefix does not exist in trie
        return node.prefix_words_list
    
    def print_trie(self):
        node = self.root
        prefix = ""
        curr_level = deque()
        next_level = deque([(prefix, node)])

        while next_level:
            curr_level = next_level
            print([(prefix, node) for prefix, node in curr_level])

            next_level = deque()
            while curr_level:
                prefix, node = curr_level.popleft()
                for char, child in node.children.items():
                    next_level.append((prefix+char, child))


class Solution:
    """
    @param words: a set of words without duplicates
    @return: all word squares
             we will sort your return value in output
    """

    def backtrack(self, square, squares):
        if len(square) == self.word_length:
            squares.append(square[:])
            return None
        
        index = len(square)
        prefix = ""
        for word in square:
            prefix += word[index]
        
        prefix_words = self.trie.find_word_with_prefix(prefix)
        # print(prefix, prefix_words)
        for word in prefix_words:
            square.append(word)
            self.backtrack(square, squares)
            square.pop()


    def word_squares(self, words):
        self.trie = Trie()
        for word in words:
            self.trie.add_word_to_trie(word)
        # trie.print_trie()
        self.word_length = len(words[0])

        squares = []
        for word in words:
            self.backtrack([word], squares)
        
        return squares
```

## Complexity Analysis
- **Trie Construction**: \( O(N \cdot L) \) where \( N \) is the number of words and \( L \) is the word length.
- **Backtracking Search**: \( O(N \cdot L) \) calls in the worst case.
- **Total Complexity**: Approximately \( O(NL) \) for a reasonable input size.

## Alternative Approaches
- **Using a HashMap** instead of a Trie for prefix lookups.
- **Iterative Breadth-First Search (BFS)** for word square construction.

## Summary
Using a Trie with DFS ensures an efficient solution by pruning invalid paths early, making the algorithm optimal for constructing word squares.

