## Question link : https://practice.geeksforgeeks.org/problems/immediate-smaller-element/0

    n = int(input())
    l = list(map(int,input().split()))
    for i in range(n-1):
        if l[i+1] < l[i]:
            print(l[i+1],end=" ")
        else:
            print(-1,end=" ")
    print(-1)
 
 
 ## Solution link : https://practice.geeksforgeeks.org/viewSol.php?subId=9600515&pid=525&user=VikasViki
