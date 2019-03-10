## Question link : https://practice.geeksforgeeks.org/problems/reverse-array-in-groups/0
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    ans = []
    for i in range(0,n,k):
        start = i
        end = i+k
        if end >= n:
            end = n
        ans.extend(reversed(l[start:end]))
    print(*ans)
 
## Solution Link : https://practice.geeksforgeeks.org/viewSol.php?subId=10612177&pid=1329&user=VikasViki
