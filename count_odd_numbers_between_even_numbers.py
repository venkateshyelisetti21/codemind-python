n=int(input())
a=list(map(int,input().split()))
c=[]
x=0
y=0
for i in range(n):
    if a[i]%2==0:
        x=i
        break
for i in range(n):
    if a[i]%2==0:
        y=i
for i in range(x+1,y):
    if a[i]%2!=0:
        c.append(a[i])
print(len(c))