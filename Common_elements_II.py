a,b=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
c=[]
for i in x:
    if i not in y:
        if i not in c:
            c.append(i)
for i in y:
    if i not in x:
        if i not in c:
            c.append(i)
print(*c)