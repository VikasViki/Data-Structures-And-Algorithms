## QUESTION LINK : https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0

def main():
    testcases = int(input())
    for _ in range(testcases):
        arr_size, desired_sum = map(int, input().split())
        arr = list(map(int, input().split()))
        start_index = index = 0
        curr_sum = 0
        while index < arr_size:
            curr_sum += arr[index]
            while curr_sum > desired_sum:
                curr_sum -= arr[start_index]
                start_index += 1
            if curr_sum ==  desired_sum:
                print(start_index+1, index+1)
                break
            index += 1
        if curr_sum != desired_sum:
            print(-1)

if __name__ == '__main__':
    main()

## SOLUTION LINK : https://practice.geeksforgeeks.org/viewSol.php?subId=271cf09e4af2975824e138d5e0cba5e8&pid=590&user=VikasViki
