n=int(input())
a=list(map(int,input().split()))
c=[]
for i in a:
    if a.count(i)==i:
        c.append(i)
if len(c):print(min(c),max(c))
else:print(-1)