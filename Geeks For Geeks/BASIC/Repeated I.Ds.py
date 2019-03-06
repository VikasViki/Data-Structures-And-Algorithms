## Question Link : https://practice.geeksforgeeks.org/problems/repeated-ids/0

    n = int(input())
    l = list(map(int,input().split()))
    ans = []
    for i in l:
        if i not in ans:
            ans.append(i)
    print(*ans)
    
## Solution link : https://practice.geeksforgeeks.org/viewSol.php?subId=10709695&pid=2570&user=VikasViki
