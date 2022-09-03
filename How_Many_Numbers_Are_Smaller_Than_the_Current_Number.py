n=int(input())
a=list(map(int,input().split()))
c=[]
for i in range(n):
    tmp=a[i]
    ctr=0
    for j in range(n):
        if tmp>a[j]:
            ctr+=1
    c.append(ctr)
for i in range(len(c)):
    print(c[i],end=' ')