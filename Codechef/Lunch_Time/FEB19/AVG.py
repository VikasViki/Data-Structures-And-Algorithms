##Question Link : https://www.codechef.com/LTIME69B/problems/AVG/

def main():
    testcases = int(input())
    for test in range(testcases):
        n,k,v = map(int,input().split())
        arr = list(map(int,input().split()))
        ans =  (v*(n+k)-sum(arr))/k
        if ans == int(ans) and ans > 0:
            print(int(ans))
        else:
            print(-1)
    
if __name__ == "__main__":
    main()

##Solution Link : https://www.codechef.com/viewsolution/23193551
