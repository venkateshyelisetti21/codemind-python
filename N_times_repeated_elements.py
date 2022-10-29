n=int(input())
a=list(map(int,input().split()))
k=int(input())
c=[]
for i in a:
    if a.count(i)==k:
        c.append(i)
c=list(set(c))
if len(c):print(*c)
else:print(-1)