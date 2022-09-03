n=int(input())
a=list(map(int,input().split()))
c=[]
p=1
e=[]
for i in range(n):
    p*=a[i]
for i in range(n):
    c.append(p)
for i in range(n):
    res=c[i]/a[i]
    e.append(int(res))
    print(e[i],end=' ')