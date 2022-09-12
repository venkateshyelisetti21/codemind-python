n=int(input())
a=list(map(int,input().split()))
c=[]
for i in a:
    if i%2==0:
        c.append(i)
for i in a:
    if i%2!=0:
        c.append(i)
print(*c)