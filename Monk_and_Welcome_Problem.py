a=int(input())
b=list(map(int,input().split()))
c=list(map(int,input().split()))
d=[]
for i in range(a):
    d.append(b[i]+c[i])
print(*d)
        