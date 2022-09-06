m,n=map(int,input().split())
c=[]
s=0
for i in range(m):
    a=list(map(int,input().split()))
    s=sum(a)
    c.append(s)
print(max(c))