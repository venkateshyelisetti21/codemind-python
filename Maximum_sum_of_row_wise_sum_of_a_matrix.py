m,n=map(int,input().split())
c=[]
for i in range(m):
    a=list(map(int,input().split()))
    tmp=sum(a)
    c.append(tmp)
print(max(c))