n=int(input())
a=list(map(int,input().split()))
c=[]
ctr=0
for i in range(n):
    c.append(len(str(a[i])))
for i in range(len(c)):
    if c[i]%2==0:
        ctr+=1
print(ctr)