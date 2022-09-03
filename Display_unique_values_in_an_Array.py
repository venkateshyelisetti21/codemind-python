n=int(input())
a=list(map(int,input().split()))
c=[]
d=[]
e=[]
for i in range(n):
    if a[i] not in c:
        c.append(a[i])
    else:
        d.append(a[i])
for i in range(len(c)):
    if c[i] not in d:
        e.append(c[i])
if len(e)==0:
    print(-1)
else:
    for i in range(len(e)):
        print(e[i],end=' ')