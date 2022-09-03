m=int(input())
a=list(map(int,input().split()))
n=int(input())
b=list(map(int,input().split()))
x=int(input())
c=[]
for i in range(n):
    for j in range(a[i],b[i]+1):
        if x==j:
            c.append(i)
print(len(c))