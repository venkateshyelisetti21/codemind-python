n=int(input())
a=list(map(int,input().split()))
c=[]
d=[]
for i in range(n):
    if a[i] not in c:
        c.append(a[i])
    else:
        d.append(a[i])
for i in range(len(d)):
    print(d[i])