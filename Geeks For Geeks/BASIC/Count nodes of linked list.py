## Question link : https://practice.geeksforgeeks.org/problems/count-nodes-of-linked-list/1


''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

"""index is the node which is to be displayed in output
  Node is defined as
class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
# Linked List class contains a Node object
class LinkedList:
    def __init__(self):
        self.head = None
This is method only submission.
 You only need to complete below method.
"""
# head is reference to head of linked list
def getCount(head):
    # Code here
    count = 1
    current = head
    while current.next != None:
        count += 1
        current = current.next
    return count

## Solution Link : https://practice.geeksforgeeks.org/viewSol.php?subId=12635292&pid=700039&user=VikasViki
