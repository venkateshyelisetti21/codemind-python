n=int(input())
a=0
b=0
c=[2,3,5,7]
for i in range(2,n):
    if n%i==0:
        break
else:
    a=True
while n:
 r=n%10
 if r in c:
     b=True
 else:b=False
 n//=10
if a==True and b==True:
    print('Mega Prime')
else:
    print('Not Mega Prime')
