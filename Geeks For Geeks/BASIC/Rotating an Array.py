## Question Link : https://practice.geeksforgeeks.org/problems/reversal-algorithm/0

    n = int(input())
    l = list(map(int,input().split()))
    d = int(input())
    ans = l[d:] + l[:d]
    print(*ans)
   
## Solution Link : https://practice.geeksforgeeks.org/viewSol.php?subId=10576890&pid=924&user=VikasViki
