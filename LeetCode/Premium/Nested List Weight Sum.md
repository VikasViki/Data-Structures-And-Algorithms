# Question Link
https://leetcode.com/problems/nested-list-weight-sum/

# Approach

# Python Code

```Python
"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation

class NestedInteger(object):
    def isInteger(self):
        # @return {boolean} True if this NestedInteger holds a single integer,
        # rather than a nested list.

    def getInteger(self):
        # @return {int} the single integer that this NestedInteger holds,
        # if it holds a single integer
        # Return None if this NestedInteger holds a nested list

    def getList(self):
        # @return {NestedInteger[]} the nested list that this NestedInteger holds,
        # if it holds a nested list
        # Return None if this NestedInteger holds a single integer
"""


class Solution(object):
    # @param {NestedInteger[]} nestedList a list of NestedInteger Object
    # @return {int} an integer
    def depthSum(self, nestedList):
        # Write your code here
        
        def get_weigth_sum(nested_list, depth):
            if nested_list.isInteger():
                return nested_list.getInteger() * depth
            
            temp_sum = 0
            for temp in nested_list.getList():
                temp_sum += get_weigth_sum(temp, depth+1)
            
            return temp_sum
        
        weight_sum = 0
        
        for val in nestedList:
            weight_sum += get_weigth_sum(val, 1)
        
        return weight_sum
        

```

# Code Explanation
