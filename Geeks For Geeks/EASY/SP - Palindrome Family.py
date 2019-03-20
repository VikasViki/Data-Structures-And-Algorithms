## Question link : https://practice.geeksforgeeks.org/problems/sp-palindrome-family/0

##Function to check whether the string is palindrome
def pal(s):
    if string[:] == string[::-1]:
        return True
    else:
        return False

for _ in range(int(input())):
    s = input()
    if pal(s):
        print("PARENT")
    else:
        even = "".join([s[i] for i in range(len(s)) if i%2 != 0])
        odd = "".join([s[i] for i in range(len(s)) if i%2 == 0])
        pal_even = pal(even)
        pal_odd = pal(odd)
        if pal_even and pal_odd:
            print("TWIN")
        elif pal_even:
            print("EVEN")
        elif pal_odd:
            print("ODD")
        else:
            print("ALIEN")

## Solution link : https://practice.geeksforgeeks.org/viewSol.php?subId=7357149&pid=3507&user=VikasViki
