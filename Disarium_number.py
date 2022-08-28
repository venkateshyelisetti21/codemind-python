tmp=int(input())
n=tmp
sum=0
a=len(str(n))
while n:
    r=n%10
    sum+=r**a
    a-=1
    n//=10
if sum==tmp:
    print(True)
else:
    print(False)