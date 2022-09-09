n=int(input())
a=list(map(int,input().split()))
x=int(input())
tmp=0
for i in range(n):
    if a[i]==x:
        tmp+=1
print(tmp)
