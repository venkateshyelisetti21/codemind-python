n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
c=[]
for i in a:
    if i>=x and i<=y:
        pass
    else:
        c.append(i)
print(sum(c))