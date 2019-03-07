## Question link : https://practice.geeksforgeeks.org/problems/multiply-left-and-right-array-sum/0
    n = int(input())
    l = list(map(int,input().split()))
    limit = n//2
    val1 = sum(l[:limit])
    val2 = sum(l[limit:])
    print(val1*val2)
   
 ## Solution link : https://practice.geeksforgeeks.org/viewSol.php?subId=5876382&pid=3247&user=VikasViki
