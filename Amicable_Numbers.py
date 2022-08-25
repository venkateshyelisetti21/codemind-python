m=int(input())
n=int(input())
sum=0
sum1=0
for i in range(1,m):
    if m%i==0:
        sum+=i
for i in range(1,n):
    if n%i==0:
        sum1+=i
if m==sum1 and n==sum:
    print('Amicable')
else:
    print('Not Amicable')
        