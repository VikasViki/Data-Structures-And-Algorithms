## Question link : https://practice.geeksforgeeks.org/problems/find-prime-numbers-in-a-range/0

prime[0] = 0
prime[1] = 0
number = 2
while number*number <= 1000002:
    if prime[number]:
        for multiples in range(2*number, 1000002, number):
            prime[multiples] = 0
    number += 1

no_of_test = int(input())
for test in range(no_of_test):
    start, end = map(int,input().split())
    for value in range(start,end+1):
        if prime[value]:
            print(value,end=" ")
    print()
    
## Solution link : https://practice.geeksforgeeks.org/viewSol.php?subId=12952208&pid=374&user=VikasViki
