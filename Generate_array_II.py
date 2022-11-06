n=int(input())
m=list(map(int,input().split()))
a=[]
b=[]
c=[]
for i in range(len(m)):
    if i%2==0:
        a.append(m[i])
    else:
        b.append(m[i])
for i in range(len(a)):
    for j in range(1,b[i]+1):
        c.append(a[i])
print(*c)