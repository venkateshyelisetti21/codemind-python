n=int(input())
a=list(map(int,input().split()))
c=[]
b=[]
for i in range(1,n+1):
    c.append(i)
for i in range(n):
    if a[i]>=0:
        if c[i] not in a:
            b.append(c[i])
print(min(b))