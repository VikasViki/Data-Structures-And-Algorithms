## Question link : https://practice.geeksforgeeks.org/problems/triangular-number/0
for number in range(1000000):
    value = (number*(number+1))//2
    if value >= 10000000:
        break
    triangular_numbers.add(value)

no_of_test = int(input())
for test in range(no_of_test):
    number = int(input())
    if number in triangular_numbers:
        print(1)
    else:
        print(0)

## Solution link : https://practice.geeksforgeeks.org/viewSol.php?subId=12925928&pid=517&user=VikasViki
