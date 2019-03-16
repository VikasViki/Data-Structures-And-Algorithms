## Question link : https://practice.geeksforgeeks.org/problems/chocolate-distribution-problem/0
    n = int(input())
    l = sorted(list(map(int,input().split())))
    m = int(input())
    ans = 10**18
    for i in range(0,n-m+1):
        temp = l[i+m-1] - l[i]
        if temp < ans:
            ans = temp
        if ans == 0:
            break
    print(ans)
            
## Solution link : https://practice.geeksforgeeks.org/viewSol.php?subId=10694773&pid=1571&user=VikasViki
