## Question link : https://practice.geeksforgeeks.org/problems/find-the-closest-number/0

    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    l.sort()
    diff = abs(l[n-1]-k)
    ans = l[n-1]
    for i in range(n-2,-1,-1):
        if abs(l[i]-k) < diff:
            ans = l[i]
            diff = abs(l[i]-k)
    print(ans)
            
   
## Solutions link : https://practice.geeksforgeeks.org/viewSol.php?subId=10685030&pid=2805&user=VikasViki
