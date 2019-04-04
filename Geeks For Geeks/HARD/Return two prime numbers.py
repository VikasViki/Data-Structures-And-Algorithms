## Question Link : https://practice.geeksforgeeks.org/problems/return-two-prime-numbers/0

prime[0] = 0
prime[1] = 0
number = 2
while number*number <= 1000000:
    if prime[number]:
        for numbers_multiple in range(2*number,1000000,number):
            prime[numbers_multiple] = 0
    number += 1

no_of_test = int(input())
for test in range(no_of_test):
    n = int(input())
    val1 = 3
    val2 = n-val1
    while True:
        if prime[val1] and prime[val2]:
            print(val1,val2)
            break
        for index in range(val1+1,1000000):
            if prime[index]:
                val1 = index
                val2 = n - val1
                break
            
## Solution link : https://practice.geeksforgeeks.org/viewSol.php?subId=12925271&pid=425&user=VikasViki
