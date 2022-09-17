def fun(n):
    s=0
    while n:
        r=n%10
        s+=(r**2)
        n//=10
    n=s
    if s>=9:
        return fun(s)
    else:
        return s
n=int(input())
tmp=fun(n)
if tmp==1 or tmp==7:
    print(True)
else:
    print(False)
        