## Question link : https://practice.geeksforgeeks.org/problems/sort-in-specific-order/0 
 
    n = int(input())
    l = sorted(list(map(int,input().split())))
    odd = []
    even = []
    for i in l:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    ans = odd[::-1] + even
    print(*ans)
   
## Solution Link : https://practice.geeksforgeeks.org/viewSol.php?subId=10722944&pid=1696&user=VikasViki
