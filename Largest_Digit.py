n=int(input())
c=0
while n:
    r=n%10
    n//=10
    if r>c:
        c=r
print(c)