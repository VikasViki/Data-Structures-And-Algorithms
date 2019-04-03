## Question link : https://practice.geeksforgeeks.org/problems/nearly-sorted-algorithm/0

no_of_test = int(input())
for test in range(no_of_test):
    n,k = map(int,input().split())
    array = list(map(int,input().split()))
    array.sort()
    print(*array)
   
## Solution link : https://practice.geeksforgeeks.org/viewSol.php?subId=12985633&pid=1967&user=VikasViki
