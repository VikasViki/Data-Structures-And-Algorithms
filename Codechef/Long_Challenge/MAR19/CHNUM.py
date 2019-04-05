## Question link : https://www.codechef.com/MARCH19B/problems/CHNUM/
def main():
    testcases = int(input())
    for test in range(testcases):
        array_size = int(input())
        scores = list(map(int,input().split()))
        positive_numbers = 0
        negative_numbers = 0
        for score in scores:
            if score > 0:
                positive_numbers += 1
            else:
                negative_numbers += 1
        if positive_numbers == 0:
            print(negative_numbers,negative_numbers)
        elif negative_numbers == 0:
            print(positive_numbers,positive_numbers)
        else:
            if positive_numbers > negative_numbers:
                print(positive_numbers,negative_numbers)
            else:
                print(negative_numbers,positive_numbers)
        
if __name__ == "__main__":
    main()
   
## Solution link : https://www.codechef.com/viewsolution/23316803
