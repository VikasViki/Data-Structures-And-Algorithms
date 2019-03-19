## Question link : https://practice.geeksforgeeks.org/problems/leaders-in-an-array/0

    n = int(input())
    l = list(map(int,input().split()))
    leader = l[n-1]
    ans = []
    ans.append(l[n-1])
    count = 1
    for i in range(n-2,-1,-1):
        if l[i] >= leader:
            ans.append(l[i])
            leader = l[i]
            count += 1
    for i in range(count-1,-1,-1):
        print(ans[i],end=" ")
    print()
            
## Solution link : https://practice.geeksforgeeks.org/viewSol.php?subId=10645814&pid=623&user=VikasViki
