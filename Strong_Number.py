x=int(input())
n=x
s=0
while n:
    r=n%10
    p=1
    for i in range(1,r+1):
        p*=i
    s+=p
    n//=10
if x==s:
    print('The number',x,'is a strong number')
else:
    print('The number',x,'is not a strong number')