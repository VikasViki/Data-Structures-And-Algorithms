##  Question link : https://practice.geeksforgeeks.org/problems/kth-smallest-element/0

for test in range(no_of_test):
    size_of_arr = int(input())
    arr = list(map(int,input().split()))
    k = int(input())
    arr.sort()
    print(arr[k-1])
   
## Solution link : https://practice.geeksforgeeks.org/viewSol.php?subId=12924732&pid=1301&user=VikasViki
