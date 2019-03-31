## Question link : https://practice.geeksforgeeks.org/problems/case-specific-sorting-of-strings/0

for test in range(no_of_test):
    
    string_length = int(input())
    case = []
    lower_characters = []
    upper_characters = []
    string = input()
    
    for index in range(string_length):
        if string[index].islower():
            case.append(0)
            lower_characters.append(string[index])
        else:
            case.append(1)
            upper_characters.append(string[index])
    lower_characters.sort()
    upper_characters.sort()
    
    sorted_string = ""
    lower_index = 0
    upper_index = 0
    
    for value in case:
        if value:
            sorted_string += upper_characters[upper_index]
            upper_index += 1
        else:
            sorted_string += lower_characters[lower_index]
            lower_index += 1
    
    print(sorted_string)
   
## Solution link : https://practice.geeksforgeeks.org/viewSol.php?subId=12952455&pid=331&user=VikasViki
