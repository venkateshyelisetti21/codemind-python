n=int(input())
a=list(map(int,input().split()))
tmp=0
for i in range(n):
    if a[i]%2==0:
        tmp=i
print(tmp)