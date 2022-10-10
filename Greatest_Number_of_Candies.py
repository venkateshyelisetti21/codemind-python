n=int(input())
a=list(map(int,input().split()))
x=int(input())
tmp=max(a)
c=[]
for i in a:
    b=i+x
    if b>=tmp:
        c.append(True)
    else:
        c.append(False)
print(*c)