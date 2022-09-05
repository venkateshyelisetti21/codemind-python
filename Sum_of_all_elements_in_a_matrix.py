m,n=map(int,input().split())
s=0
for i in range(m):
    a=list(map(int,input().split()))
    s+=sum(a)
print(s)