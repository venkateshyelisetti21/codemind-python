def fun(n):
    s=0
    while n:
        r=n%10
        s=s+r
        n=n//10
        
    n=s
    
    if s>=9:
        return fun(s)
    else:
        return s
        
n=int(input())
print(fun(n))
