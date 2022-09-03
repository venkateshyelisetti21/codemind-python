n=int(input())
a=list(map(int,input().split()))
c=[]
d=[]
for i in range(n):
    if a[i]!=0:
        c.append(a[i])
    else:
        d.append(a[i])
for i in range(len(c)):
    print(c[i],end=' ')
for i in range(len(d)):
    print(d[i],end=' ')