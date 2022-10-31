def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

def lcm(a, b):
    return a//gcd(a,b)*b

q=int(input())
while q:
    q-=1
    n, a, b, k = list(map(int, input().split(' ')))
    a=(n//a) + (n//b-2*n//lcm(a, b))
    if a>=k:print("Win")
    else:print("Lose")