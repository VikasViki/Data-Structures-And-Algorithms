## Question link : https://practice.geeksforgeeks.org/problems/search-an-element-in-an-array/0    
    
    n = int(input())
    l = list(map(int,input().split()))
    x = int(input())
    for i in range(n):
        if l[i] == x:
            print(i)
            break
    else:
        print(-1)
     
## Solution Link : https://practice.geeksforgeeks.org/viewSol.php?subId=7643246&pid=77&user=VikasViki
