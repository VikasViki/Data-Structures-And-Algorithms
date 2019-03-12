## Question link : https://practice.geeksforgeeks.org/problems/transform-to-prime/0

prime[0] = 0
prime[1] = 0
p = 2
while p*p <= 1000000:
    if prime[p]:
        for i in range(2*p,1000001,p):
            prime[i] = 0
    p += 1
    

for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    ans = sum(l)
    count = 0
    while not prime[ans]:
       ans += 1
       count += 1
    print(count)
    
 ## Solution link : https://practice.geeksforgeeks.org/viewSol.php?subId=10658684&pid=2452&user=VikasViki
