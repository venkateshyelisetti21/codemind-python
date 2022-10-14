n=int(input())
l=len(str(n))
a=[2,3,5,7]
b=0
ctr=0
for i in range(2,int(n**.5) +1):
    if n%i==0:
        break
else:
   b=True
if b==True:
    while n:
        r=n%10
        if r in a:
            ctr+=1
        n//=10
    if l==ctr:
        print('Mega Prime')
    else:print('Not Mega Prime')
else:print('Not Mega Prime')