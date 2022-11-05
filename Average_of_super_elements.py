n=int(input())
a=list(map(int,input().split()))
c=[]
for i in a:
    if a.count(i)==i:
        c.append(i)
c=list(set(c))
if len(c):
    avg=sum(c)/len(c)
    res="{:.2f}".format(avg)
    print(res)
else:print(-1)