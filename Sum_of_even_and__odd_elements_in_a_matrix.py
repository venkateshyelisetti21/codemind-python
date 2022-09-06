m,n=map(int,input().split())
x=0
y=0
for i in range(m):
    a=list(map(int,input().split()))
    for i in range(n):
        if a[i]%2==0:
            x+=a[i]
        else:
            y+=a[i]
print(x,y)