n=int(input())
a=list(map(int,input().split()))
x=int(input())
c=[]
b=0
d=[-1,-1]
for i in range(n):
    if a[i]==x:
        c.append(i)
        break
for i in range(n):
    if a[i]==x:
        b=i
c.append(b)
if len(c)<2:
    for i in range(len(d)):
        print(d[i],end=' ')
else:
    for i in range(len(c)):
        print(c[i],end=' ')