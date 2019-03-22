## Question link : https://practice.geeksforgeeks.org/problems/product-of-array-element/1

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
# arr is the array
# n is the number of element in array
# mod= modulo value
def product(arr,n,mod):
    # your code here
    ans = 1
    for value in arr:
        ans *= value
    return ans%mod
   
## Solution link : https://practice.geeksforgeeks.org/viewSol.php?subId=12966162&pid=700714&user=VikasViki
