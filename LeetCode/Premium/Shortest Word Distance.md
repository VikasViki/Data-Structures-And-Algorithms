# Question Link
https://leetcode.com/problems/shortest-word-distance/

# Approach

# Python Code

```Python
class Solution:
    """
    @param words: a list of words
    @param word1: a string
    @param word2: a string
    @return: the shortest distance between word1 and word2 in the list
    """
    
    def shortestDistance(self, words, word1, word2):
        # Write your code here
        word1_indices = []
        word2_indices = []
        for index, word in enumerate(words):
            if word == word1:
                word1_indices += [index]
            elif word == word2:
                word2_indices += [index]
        
        shortest_distance =  float('inf')
        
        for word1_index in word1_indices:
            for word2_index in word2_indices:
                shortest_distance = min(shortest_distance, abs(word1_index-word2_index))
        
        return shortest_distance
 ```

# Code Explanation
