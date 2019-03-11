## Question link : https://practice.geeksforgeeks.org/problems/print-an-array-in-pendulum-arrangement/0

    n = int(input())
    l = list(map(int,input().split()))
    l.sort()
    left = []
    right = []
    for i in range(n):
        if i%2 == 0:
            left.append(l[i])
        else:
            right.append(l[i])
    ans = left[::-1] + right
    print(*ans)
   
## Solution link : https://practice.geeksforgeeks.org/viewSol.php?subId=10587932&pid=1947&user=VikasViki
