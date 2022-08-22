n=int(input())
sum=0
pro=1
while n:
    r=n%10
    sum+=r
    pro*=r
    n//=10
if sum==pro:
    print('Spy Number')
else:
    print('Not Spy Number')