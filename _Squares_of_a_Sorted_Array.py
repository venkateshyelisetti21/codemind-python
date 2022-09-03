n=int(input())
a=list(map(int,input().split()))
tmp=0
c=[]
for i in range(n):
    tmp=a[i]*a[i]
    c.append(tmp)
c.sort()
for i in range(len(c)):
    print(c[i],end=' ')
    