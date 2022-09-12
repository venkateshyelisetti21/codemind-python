m,n=map(int,input().split())
c=[]
for i in range(m):
    a=list(map(int,input().split()))
    tmp=sum(a)
    c.append(tmp)
x=0
y=0
for i in range(len(c)):
    if i%2==0:
        x+=c[i]
    else:
        y+=c[i]
print(x,y)
        