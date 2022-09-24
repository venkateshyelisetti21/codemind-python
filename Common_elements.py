a,b=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
c=[]
for i in x:
    for j in y:
        if i==j:
            if i not in c:
                c.append(i)
print(*c)