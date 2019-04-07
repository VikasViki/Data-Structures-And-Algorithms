## Question link : https://www.codechef.com/problems/NBONACCI

from sys import stdin
def main():
    n,q = map(int,stdin.readline().split())
    arr = list(map(int,stdin.readline().split()))
    f = [0,arr[0]]
    xor = arr[0]^arr[1]
    f.append(xor)
    for index in range(2,n):
        xor ^= arr[index]
        f.append(xor)
    for query in range(q):
        k = int(stdin.readline())
        if k <= n:
            print(f[k])
        else:
            print(f[k%(n+1)])
            
if __name__ == "__main__":
    main()
   
## Solution link : https://www.codechef.com/viewsolution/23675823
