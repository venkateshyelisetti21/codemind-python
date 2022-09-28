n=int(input())
a=list(map(int,input().split()))
c=[]
d=[]
e=[]
for i in a:
    if i not in c:
        c.append(i)
    else:
        d.append(i)
for i in c:
    if i not in d:
        e.append(i)
if len(e):print(max(e))
else:print(-1)