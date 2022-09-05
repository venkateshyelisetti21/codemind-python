m,n=map(int,input().split())
c=[]
for i in range(m):
    s=0
    a=list(map(int,input().split()))
    s+=sum(a)
    c.append(s)
for i in range(len(c)):
    print(c[i],end=' ')