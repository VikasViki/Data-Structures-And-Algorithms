## Question link : https://practice.geeksforgeeks.org/problems/sum-of-bit-differences/0

def bit_difference(number1, number2):
    xor_of_numbers = number1 ^ number2
    no_of_diff_bits = bin(xor_of_numbers).count('1')
    return no_of_diff_bits
    
no_of_test = int(input())

for test in range(no_of_test):
    array_size = int(input())
    array = list(map(int,input().split()))
    sum_of_bit_diff = 0
    
    for index1 in range(array_size):
        for index2 in range(index1+1,array_size):
            
            sum_of_bit_diff += bit_difference(array[index1],array[index2])
    
    print(sum_of_bit_diff*2)
    
## Solution link : https://practice.geeksforgeeks.org/viewSol.php?subId=12985586&pid=345&user=VikasViki
