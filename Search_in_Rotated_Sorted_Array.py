n=int(input())
a=list(map(int,input().split()))
x=int(input())
c=0
for i in range(n):
    if a[i]==x:
        c=i
        break
else:
    c=-1
print(c)
