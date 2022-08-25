n=int(input())
a=[]
c=0
while n:
    r=n%10
    if r not in a:
        a.append(r)
    else:
        c+=1
    n//=10
if c==0:
    print('Unique Number')
else:
    print('Not Unique Number')