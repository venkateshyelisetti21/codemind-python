def fib(n):
    a=0
    b=1
    while b<n:
        c=a+b
        a=b
        b=c
    if a==n or b==n:
        return True
    else:
        return False
def nearfib(n):
    a=n
    b=n
    while fib(a)==False:
        a=a-1
    while fib(b)==False:
        b=b+1
    if abs(a-n)>abs(b-n):
        return b
    elif abs(a-n)==abs(b-n):
        return str(a)+" "+str(b)
    else:
        return a
print(nearfib(int(input())))