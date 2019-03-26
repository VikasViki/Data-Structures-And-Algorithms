## Question link : https://practice.geeksforgeeks.org/problems/excel-sheet/0

for _ in range(no_of_testcases):
    ans = ""
    number = int(input())
    while number > 0:
        remainder = number%26
        if remainder == 0:
            ans += "Z"
            number = number // 26 - 1
        else:
            ans += chr(remainder + 64)
            number = number // 26
    print(ans[::-1])
 
 ## Solution link : https://practice.geeksforgeeks.org/viewSol.php?subId=11903425&pid=117&user=VikasViki
