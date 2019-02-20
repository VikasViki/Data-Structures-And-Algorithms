def gcd(x,y):
    while y:
        x,y = y,x%y
    return x

def lcm(a,b):
    return (a*b) // gcd(a,b)

for _ in range(int(input())):
    n,a,b,k = map(int,input().split())
    count = 0
    a_count =  n // a
    b_count = n // b
    ab_count = n // lcm(a,b)
    
    #print(a_count,b_count,ab_count*2)
    
    if (a_count + b_count - (ab_count*2)) >= k:
        print("Win")
    else:
        print("Lose")
