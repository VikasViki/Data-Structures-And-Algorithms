## Question link : https://practice.geeksforgeeks.org/problems/find-second-largest-element/0

    n = int(input())
    l = list(set(map(int,input().split())))
    if len(l)<2:
        print(-1)
    else:
        l.sort()
        print(l[-2])
    
## Solution link : https://practice.geeksforgeeks.org/viewSol.php?subId=4411217&pid=2040&user=VikasViki
