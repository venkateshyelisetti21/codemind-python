n=int(input())
a=list(map(int,input().split()))
x=[]
y=[]
z=[]
for i in range(n):
    if i%2==0:
       x.append(a[i])
    else:
        y.append(a[i])
for i in range(len(x)):
    for j in range(x[i]):
        z.append(y[i])
print(*z)